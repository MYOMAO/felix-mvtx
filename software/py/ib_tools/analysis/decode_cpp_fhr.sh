(
  set -eu -o pipefail

  usage()
  {
     echo "Usage: $( basename "${BASH_SOURCE[0]}" ) [options]"
     echo "Options:"
     echo "-f <SUBRACK | feeid>  SUBRACK {FLx0..FLX5, TEL} or feeid."
     echo "-n <n_event>          number of event to analyze from evt file."
     echo "-p <PACKET_ID>        packetID, when single feeid is used."
     echo "-t <TEST>             test. default = FHR"
     exit 0
  }

  exit_abnormal()
  {
    usage
    exit 1
  }

  PACKETS=()
  INPUTS=()
  TEST=0
  N_EVENTS=0
  while getopts ":f:p:t:" OPT; do
    case "$OPT" in
      f )
          if [[ x"$OPTARG" == x"FLX0" ]]; then
            PACKETS=( 2001 2002 )
            INPUTS=( "0 256 512 4099 4355 4611 8198 8199 8454 8455 8710 8711"
                     "1 257 513 4100 4356 4612 8200 8201 8456 8457 8712 8713" )
          elif [[ x"$OPTARG" == x"FLX1" ]]; then
            PACKETS=( 2011 2012 )
            INPUTS=( "2 258 514 4101 4102 4357 4358 4613 4614 8202 8458 8714"
                     "3 259 515 4103 4359 4615 8203 8204 8459 8460 8715 8716" )
          elif [[ x"$OPTARG" == x"FLX2" ]]; then
            PACKETS=( 2021 2022 )
            INPUTS=( "4 260 516 4104 4105 4360 4361 4616 4617 8205 8461 8717"
                     "5 261 517 4106 4362 4618 8206 8207 8462 8463 8718 8719" )
          elif [[ x"$OPTARG" == x"FLX3" ]]; then
            PACKETS=( 2031 2032 )
            INPUTS=( "6 262 518 4107 4363 4619 8208 8209 8464 8465 8720 8721"
                     "7 263 519 4108 4364 4620 8210 8211 8466 8467 8722 8723" )
          elif [[ x"$OPTARG" == x"FLX4" ]]; then
            PACKETS=( 2041 2042 )
            INPUTS=( "8 264 520 4109 4110 4365 4366 4621 4622 8192 8448 8704"
                     "9 265 521 4111 4367 4623 8193 8194 8449 8450 8705 8706" )
          elif [[ x"$OPTARG" == x"FLX5" ]]; then
            PACKETS=( 2051 2052 )
            INPUTS=( "10 266 522 4096 4097 4352 4353 4608 4609 8195 8451 8707"
                     "11 267 523 4098 4354 4610 8196 8197 8452 8453 8708 8709" )
          elif [[ x"$OPTARG" == x"TEL" ]]; then
            PACKETS=( 2001 2002 )
            INPUTS=( "8212 8213 8214 8215 8468 8469 8470 8471 8724 8725 8726 8727"
                     "8216 8217 8218 8219 8472 8473 8474 8475 8728 8729 8730 8731" )
          else
            PACKETS=
            INPUTS=( $OPTARG )
          fi
          ;;
    n )
        N_EVENTS=${N_EVENTS}
        ;;
    p )
        PACKETS=${PACKETS:="$OPTARG"}
        ;;
    t )
        TEST=${OPTARG}
        ;;
    : )
        echo "ERROR: -${OPTARG} requires an argument.";
        exit_abnormal
        ;;
    \? )
        echo "ERROR: unknow option"
        exit_abnormal
        ;;
    esac
  done
  shift $((OPTIND - 1))

  [[ $# == 0 ]] && { echo "ERROR: no files entered."; exit_abnormal; }
  FILES=$@

  (( ${#PACKETS[@]} )) || { echo "ERROR: SUBRACK or feeid no entered"; exit_abnormal; }
  (( ${#INPUTS[@]} )) || { echo "ERROR: SUBRACK or feeid no entered"; exit_abnormal; }

#time ddump -s -g -n 0 -p 2001 $FILE  | /home/mvtx/felix-mvtx/software/cpp/decoder/mvtx-decoder -p test -t $TEST -f 8213
  for iPACKET in "${!PACKETS[@]}"; do
    for FEEID in ${INPUTS[$iPACKET]}; do
      CMD=""
      for FILE in "${FILES[@]}"; do
        CMD=${CMD:+"$CMD && ddump -g -s -p ${PACKETS[$iPACKET]} -n ${N_EVENTS} $FILE"}
        CMD=${CMD:="( ddump -g -s -p ${PACKETS[$iPACKET]} -n ${N_EVENTS} $FILE"}
      done
      CMD="$CMD ) | /home/mvtx/felix-mvtx/software/cpp/decoder/mvtx-decoder -f $FEEID -t ${TEST} -p 'fhrana'"
      echo $CMD
    time eval $CMD
    done
  done
)
