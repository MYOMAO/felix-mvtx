<project name="ITS-RU" version="1.1">
    <ProjectDirectory>
        .
    </ProjectDirectory>
    <View>
        ChainView
    </View>
    <LiberoTargetDevice>

    </LiberoTargetDevice>
    <LogFile>
        ITS-RU.log
    </LogFile>
    <SerializationOption>
        Skip
    </SerializationOption>
    <programmer status="enable" type="FlashPro5" revision="UndefRev" connection="usb2.0">
        <name>
            S201R1NHU
        </name>
        <id>
            S201R1NHU
        </id>
    </programmer>
    <configuration>
        <Hardware>
            <FlashPro>
                <TCK>
                    4000000
                </TCK>
                <Vpp/>
                <Vpn/>
                <Vddl/>
                <Vdd>
2500                </Vdd>
            </FlashPro>
            <FlashProLite>
                <TCK>
                    4000000
                </TCK>
                <Vpp/>
                <Vpn/>
            </FlashProLite>
            <FlashPro3>
                <TCK>
                    4000000
                </TCK>
                <Vpump/>
                <ClkMode>
                    FreeRunningClk
                </ClkMode>
            </FlashPro3>
            <FlashPro4>
                <TCK>
                    4000000
                </TCK>
                <Vpump/>
                <ClkMode>
                    FreeRunningClk
                </ClkMode>
            </FlashPro4>
            <FlashPro5>
                <TCK>
                    4000000
                </TCK>
                <Vpump/>
                <ClkMode>
                    FreeRunningClk
                </ClkMode>
                <ProgrammingMode>
                    JTAGMode
                </ProgrammingMode>
            </FlashPro5>
        </Hardware>
        <Device type="ACTEL">
            <Name>
                A3PE600L
            </Name>
            <Custom>
                A3PE(L)/AGLE/RT3PE600L
            </Custom>
            <Algo type="PDB">
                <filename>
                    dummy.pdb
                </filename>
                <local>
                    bitfile.pdb
                </local>
                <SelectedAction>
                    PROGRAM
                </SelectedAction>
            </Algo>
        </Device>
        <Algo type="unknown">
            <irlength>
                0
            </irlength>
            <MaxTCK>
                0
            </MaxTCK>
        </Algo>
    </configuration>
</project>
