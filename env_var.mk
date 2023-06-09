#
# File included by other make scripts
# Contains fixed paths and other configurable settings
#
# Export variables so they can be reached from Tcl scripts also
#
# To change the default paths, duplicate this file and call it env_var_local.mk
# Changes in this file will persist, but not be committed to git
#

#export VIVADO_VER=2016.4
export VIVADO_VER=2020.2
#export VIVADO_YEAR=2016
export VIVADO_YEAR=2020
# Remember to update the version of the ipcores in sim/scripts/RUv1_top.tcl when changing version

ifeq ($(OS),Windows_NT)
  export VIVADO_PATH=c:/Xilinx/Vivado
  export MODELSIM_PATH=c:/mentor/questasim64_10.6b/win64
else
  export VIVADO_PATH=/opt/Xilinx/Vivado
  export MODELSIM_PATH=/opt/mentor/modelsim/106c/modeltech/bin
  export IUS_PATH=${CDS_INCV}/tools/bin
  export FP_PATH=/opt/microsemi/Program_Debug_v11.9/Program_Debug/bin
endif

# Exported so it can be used in modelsim tcl script
export SIMLIB_MODELSIM_PATH=${VIVADO_PATH}/${VIVADO_VER}/simlib_modelsim
