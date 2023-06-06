# DDG

This module generates GBT data, either in packet or continuous mode. In continuous mode a counter is sent as payload. If the 
--tpc-emu flag is used, instead of the counter a TPC style stream is sent which consists of 8 header frame with pre-defined pattern, and then random data generated by a PRNG. The reset in this mode is 8-frame aligned meaning it is actually asserted only on the next 8-frame boundary.


In packet mode standard packets are generated (4 RDH words, then payload). The maximum size of a packet indluding the RDH is 512 words. SOx and EOx trigger RDH-only packets (size is 4 words). For each HB Frame a RDH-only header and trailer are sent. By default internal trigger is used which is always high, so packets are sent continuously. If TTC is selected as trigger source, the actual bit that triggers a packet can be selected from TTC\_DATA[15:0]. During sending the payload triggers are ignored, except HB. If meanwhile a HB trigger occurs, after sending the full payload of the previous packet the HB trailer and header (for the next HBF) are sent immediately. Packets can be configured in several ways, for the available options see below.


With each sent packet an 32-bit counter increases, which can be read for debugging purposes.

Options:


|Option | Description |
|------------------------|-------------------------------------|
|  -h, --help            |Show help message and exit           |
|  -i ID, --id ID        |PCIe address, e.g. 06:0.0. It can be retrieved by using the o2-roc-list-cards command |
|  -v, --verbose         |Increase output verbosity |
|  -c {continuous,packet}, --configure {continuous,packet} | Configure ddg mode (`continuous` or `packet`). Default is `continuous` |
|  -tpc, --tpc-emu       | Enables TPC data format (in continuous mode): 8-frame pre-defined header and then payload.
|  -z, --rnd-size	 | Generate packets with random size (in `packet` mode) |
|  -pllimit PAYLOAD\_LIMIT | --payload-limit PAYLOAD\_LIMIT | Max size of payload in words. Min 0, max 508 |
|  -rndrange RND\_RANGE, --rnd-range RND\_RANGE | Min 1, max PAYLOAD\_LIMIT+4, AND must be a power of 2. Resulting payload size range in gbt words: [max(0, PAYLOAD\_LIMIT - RND\_RANGE), PAYLOAD\_LIMIT] |
|  -w, --rnd-idle-btw	 | Generate packets with random number of `IDLE` words between the packets   |
|  -il, --idle-length    | Sets the number of IDLEs between packets (if it's not set to random) to control throughput  |
|  -n, --rnd-idle-in	 | Generate packets with random number of `IDLE` words between payload words |
|  -t {internal,ttc}, --trigger {internal,ttc}| Select trigger source between `internal` or `ttc`, default value is `internal`. | 
|  -ts TRIGGER\_MASK, --trigger-select TRIGGER\_MASK|If the selected trigger source is `ttc`, it selects which TTCPON bit triggers the packets (from TTC\_DATA[31:0]) The default value of the 32-bit mask is 0xFFFFF87C meaning that hb, orbit, sox, eox don't trigger regular packets. 
|  -p, --pause           | Pause ddg  | 
|  -u, --resume          | Resume ddg |
|  -b, --burst           | Send a burst of packets and then stop     |
|  -l BURST\_LENGTH, --burst-length BURST\_LENGTH | Sets the number of packets sent in 1 burst (max 8)
|  -s, --sent            | Print the 8-bit packet counter  	     |
|  -r, --reset		 | Asserts then de-asserts the reset signal  |