#!/usr/bin/env python3.9

from .ibtest import *

class FelixTriggered(IBTest):
    def __init__(self, name="FelixTriggered", cru=FLX, ru_list=None):
        IBTest.__init__(self, name, cru, ru_list)

        self.duration = 300 # s
        # set to ~90us
        self.set_trigger_period(3564*25) # ns 3564*25 ns -> 11 kHz
        self.trigger_mode = TriggerMode.TRIGGERED
        self.trigger_source = trigger_handler.TriggerSource.GBTx2
        self.send_pulses = False

    def _configure_stave(self, ru):
        ch = Alpide(ru, chipid=0xF) # broadcast
        configure_chip(ch, chargepump=8, driver=8, preemp=8,
                       linkspeed=self.link_speed,
                       strobe_duration_ns=200,
                       pulse_duration_ns=self.trigger_period*0.5, # not relevant
                       pulse2strobe=self.send_pulses,
                       analogue_pulsing=1)
        configure_dacs(ch, self.vbb)
        ch.unmask_all_pixels()

    def run_step(self):
        ''' This method is called when running via RCS '''
        elapsed_time = round(time.time()-self._trigger_start_time)
        if time.time()-self._last_log_time > self._logging_period:
            self.log.info('Elapsed time: {} of {} s'.format(elapsed_time, self.duration))
            counters = self.log_during_run('RUN_STEP')

            _,bad_counters,_ = print_counters_ru_datapathmon_summary(counters['RUs'])
            if bad_counters:
                self.log.warning(f'RU datapath counters show errors! {bad_counters}')
            if self._stop_on_ru_counter_errors and len(bad_counters) and not self.dry_run:
                self.log.error('RU datapath counters not OK! Stopping!')
                return (-1, -1)

            _,bad_counters = print_status_ru_readout_master_summary(counters['RUs'])
            if 'FERO_OKAY' in bad_counters:
                self.log.warning(f"RU readout master shows errors! {bad_counters['FERO_OKAY']}")
            if 'FERO_OKAY' in bad_counters and not self.dry_run:
                self.log.error('RU readout master FERO NOT OKAY! Stopping!')
                return (-1, -1)

            self._last_log_time = time.time()
        if self.n_triggers > 0:
            return (self.triggers_sent, self.n_triggers)
        elif self.duration > 0:
            return (elapsed_time, self.duration)
        else:
            return (-1, 0)
