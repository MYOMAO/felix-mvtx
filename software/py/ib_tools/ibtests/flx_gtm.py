#!/usr/bin/env python3.9

from .ibtest import *

class FelixGTMContinuous(IBTest):
    def __init__(self, name="FelixGTMContinuous", cru=FLX, ru_list=None):
        IBTest.__init__(self, name, cru, ru_list)

        self.duration = 300 # s
        # set to ~10us
        self.set_trigger_period(3564*25/9) # ns 3564*25 ns -> 11 kHz
        self.trigger_mode = TriggerMode.CONTINUOUS
        self.trigger_source = trigger_handler.TriggerSource.GBTx2
        self.send_pulses = False

    def _configure_stave(self, ru):
        ch = Alpide(ru, chipid=0xF) # broadcast
        configure_chip(ch, chargepump=8, driver=8, preemp=8,
                       linkspeed=self.link_speed,
                       strobe_duration_ns=self.trigger_period-200,
                       pulse_duration_ns=self.trigger_period*0.5, # not relevant
                       pulse2strobe=self.send_pulses,
                       analogue_pulsing=1)
        configure_dacs(ch, self.vbb)
        ch.unmask_all_pixels()

    def start_of_trigger(self):
        self.log.info('Starting trigger via GTM in {} mode at {:.1f} kHz on source {}'.format(
            self.trigger_mode.name,
            1e6/self.trigger_period,
            self.trigger_source.name) )
        hb_period = (self.cru.ttc.get_heartbeat_period()+1)*25.00
        for ru in self.ru_list:
            th_period = ru.trigger_handler.get_trigger_period()*6.25
            assert hb_period % th_period == 0, \
                "HB period {} not a multiple of RU {} trigger period {}".format(hb_period,ru.name, th_period)

        # Now configure FELIX GTM emulator to accept modebits and start continuous mode running
        self.cru.ttc.set_emulator_cont_mode(use_gtm=True)
        # wait for user input to start running
        input("Start run vi GTM, then press return...")

        self._trigger_start_time = time.time()
        self._triggering = True


class FelixGTMTriggered(IBTest):
    def __init__(self, name="FelixGTMTriggered", cru=FLX, ru_list=None):
        IBTest.__init__(self, name, cru, ru_list)

        self.duration = 300 # s
        self.set_trigger_period(3564*25) # ns 3564*25 ns -> 11 kHz
        self.trigger_mode = TriggerMode.TRIGGERED
        self.trigger_source = trigger_handler.TriggerSource.GBTx2
        self.send_pulses = False

    def _configure_stave(self, ru):
        ch = Alpide(ru, chipid=0xF) # broadcast
        configure_chip(ch, chargepump=8, driver=8, preemp=8,
                       linkspeed=self.link_speed,
                       strobe_duration_ns=self.trigger_period-200,
                       pulse_duration_ns=self.trigger_period*0.5, # not relevant
                       pulse2strobe=self.send_pulses,
                       analogue_pulsing=1)
        configure_dacs(ch, self.vbb)
        ch.unmask_all_pixels()

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

    def start_of_trigger(self):
        self.log.info('Starting trigger via GTM in {} mode at {:.1f} kHz on source {}'.format(
            self.trigger_mode.name,
            1e6/self.trigger_period,
            self.trigger_source.name) )
        # Now configure FELIX GTM emulator to accept modebits and start continuous mode running
        self.cru.ttc.set_emulator_trig_mode(mode="manual", use_gtm=True)
        # wait for user input to start running
        input("Start run vi GTM, then press return...")

        self._trigger_start_time = time.time()
        self._triggering = True

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
