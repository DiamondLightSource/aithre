import json
import httpx
import asyncio

async def generalStatus(self):
    """Fetch general status asynchronously"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{self.carbideEndPoint}/v1/Basic/GeneralStatus")
        return response

async def getInfo(self):
    """Gets text-based status, warnings, and errors asynchronously"""
    async with httpx.AsyncClient() as client:
        # Fetch general status, warnings, and errors concurrently
        general_status, warnings, errors = await asyncio.gather(
            self.generalStatus(),
            client.get(f"{self.carbideEndPoint}/v1/Basic/Warnings"),
            client.get(f"{self.carbideEndPoint}/v1/Basic/Errors")
        )
        
        # Handle General Status
        if general_status.status_code == 200:
            print(general_status.text)
        
        # Handle Warnings
        if warnings.status_code == 200:
            print(warnings.text)
        
        # Handle Errors
        if errors.status_code == 200:
            print(errors.text)

async def actualValues(self):
    """Fetch and process actual values asynchronously using httpx"""
    endpoints = {
        "actualattenuatorpercentage": f"{self.carbideEndPoint}/v1/Basic/ActualAttenuatorPercentage",
        "actualoutputenergy": f"{self.carbideEndPoint}/v1/Basic/ActualOutputEnergy",
        "actualoutputfrequency": f"{self.carbideEndPoint}/v1/Basic/ActualOutputFrequency",
        "actualoutputpower": f"{self.carbideEndPoint}/v1/Basic/ActualOutputPower",
        "actualpulseduration": f"{self.carbideEndPoint}/v1/Basic/ActualPulseDuration",
        "actualPpdivider": f"{self.carbideEndPoint}/v1/Basic/ActualPpDivider",
        "actualshutterstate": f"{self.carbideEndPoint}/v1/Basic/ActualShutterState",
        "actualrafrequency": f"{self.carbideEndPoint}/v1/Advanced/ActualRaFrequency",
        "actualstateid": f"{self.carbideEndPoint}/v1/Advanced/ActualStateId",
        "actualharmonic": f"{self.carbideEndPoint}/v1/Basic/ActualHarmonic",
    }

    async with httpx.AsyncClient() as client:
        # Fetch all data concurrently
        responses = await asyncio.gather(
            *(client.get(url) for url in endpoints.values())
        )

    # Process and store responses
    for key, response in zip(endpoints.keys(), responses):
        if response.status_code == 200:
            value = response.text.strip()
            setattr(self, key, value)  # Dynamically set attribute on `self`

            # Log or process specific keys
            if key == "actualattenuatorpercentage":
                self.actualattenuatorpercentage_float = float(value)
                print(f"Attenuator percentage: {value}%")
            elif key == "actualoutputenergy":
                print(f"Output energy: {value} uJ")
            elif key == "actualoutputfrequency":
                print(f"Output frequency: {value} kHz")
            elif key == "actualoutputpower":
                print(f"Output power: {value} W")
            elif key == "actualpulseduration":
                print(f"Pulse duration: {value} fs")
            elif key == "actualPpdivider":
                print(f"Pulse picker divider: {value}")
            elif key == "actualshutterstate":
                print(f"Shutter state: {value}")
            elif key == "actualrafrequency":
                print(f"RA frequency: {value} Hz")
            elif key == "actualstateid":
                print(f"State ID no.: {value}")
            elif key == "actualharmonic":
                try:
                    self.wavelength = int(1030 / int(value))
                    print(f"Using harmonic {value}, {self.wavelength}nm")
                except ValueError:
                    print("Harmonic is likely 0 as not running")
        else:
            print(f"Unable to fetch {key}: {response.status_code}")

async def serialNumber(self):
    """Fetch and display the laser serial number asynchronously using httpx"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{self.carbideEndPoint}/v1/Basic/SerialNumber")

    if response.status_code == 200:
        self.serialnumber = response.text.strip()
        print(f"Laser Serial Number: {self.serialnumber}")
    else:
        print("Not sure about serial number")

async def isOutputEnabled(self):
    """Check if the output is enabled asynchronously using httpx"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{self.carbideEndPoint}/v1/Basic/IsOutputEnabled")

    if response.status_code == 200:
        self.isoutputenabled = response.text.strip()  # Store the value as a string
        if self.isoutputenabled == "true":
            print("Output is open")
        elif self.isoutputenabled == "false":
            print("Output is closed")
    else:
        print("Not sure about output status")

async def getLastExecutedPresetIndex(self):
    """Fetch the last executed preset index asynchronously using httpx"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{self.carbideEndPoint}/v1/Basic/LastExecutedPresetIndex"
        )

    if response.status_code == 200:
        self.lastexecutedpresetindex = response.text.strip()  # Store the value
        print(f"Last executed preset index was {self.lastexecutedpresetindex}")
    else:
        print("Error getting last executed preset index")

async def selectAndApplyPreset(self, preset="1"):
    """Select preset, apply preset, and wait for the laser to become operational

    Args:
        preset (str, optional): Preset to use as set in GUI. Defaults to "1".
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{self.carbideEndPoint}/v1/Basic/SelectedPresetIndex")

    if response.status_code == 200:
        self.currentpreset = response.text.strip()
        print(f"Current preset is {self.currentpreset}")
    else:
        print("No idea what current preset is")

    print(f"Requesting preset {preset}")
    presetNumber = int(preset)

    async with httpx.AsyncClient() as client:
        select_response = await client.put(
            f"{self.carbideEndPoint}/v1/Basic/SelectedPresetIndex",
            data=json.dumps(presetNumber),
            headers=self.requestHeaders,
        )

    if select_response.status_code == 200:
        print(f"Preset {preset} has been set, applying...")
        async with httpx.AsyncClient() as client:
            apply_response = await client.post(
                f"{self.carbideEndPoint}/v1/Basic/ApplySelectedPreset",
                headers=self.requestHeaders,
            )

        await asyncio.sleep(2)

        if apply_response.status_code == 200:
            await self.waitForLaserOperational()
            print("Successfully applied!")
        elif apply_response.status_code == 403:
            print("Could not apply preset")
        else:
            print("Error applying preset")
    elif select_response.status_code == 403:
        print("Preset doesn't exist. Check available presets")
    else:
        print("Error setting preset")
        
async def changeOutput(self, state="close"):
    """_summary_

    Args:
        state (str, optional): _description_. Defaults to "close".
    """
    print(f"Requesting output {state}")
    async with httpx.AsyncClient() as client:
        if state == "enable":
            response = await client.post(f"{self.carbideEndPoint}/v1/Basic/EnableOutput", headers=self.requestHeaders)
            self.enableoutput = response
            if response.status_code == 200:
                print("Output enabled")
            elif response.status_code == 403:
                print("Cannot enable output, check state")
            else:
                print("Set output enable error")
        elif state == "close":
            response = await client.post(f"{self.carbideEndPoint}/v1/Basic/CloseOutput", headers=self.requestHeaders)
            self.closeoutput = response
            if response.status_code == 200:
                print("Output closed")
            elif response.status_code == 403:
                print("Laser not running anyway")
            else:
                print("Set output close error")

async def closeOutput(self):
    async with httpx.AsyncClient() as client:
        self.closeoutput = await client.post(
            f"{self.carbideEndPoint}/v1/Basic/CloseOutput",
            headers=self.requestHeaders,
        )

async def waitForLaserOperational(self):
    """Wait for laser to reach operational state, break if in failure state"""
    await self.actualStateName()
    while self.actualstatename.text.strip() != '"Operational"':
        print(self.actualstatename.text.strip())
        await asyncio.sleep(1)
        await self.actualStateName()
        if self.actualstatename.text.strip() == '"Failure"':
            print("Laser in failure state. Stopping...")
            break
    if self.actualstatename.text.strip() == '"Operational"':
        print("Laser in operational state, ready to enable output")

async def actualStateName(self):
    """Get current state of laser"""
    async with httpx.AsyncClient() as client:
        self.actualstatename = await client.get(
            f"{self.carbideEndPoint}/v1/Basic/ActualStateName"
        )

async def goToStandby(self):
    """_summary_"""
    async with httpx.AsyncClient() as client:
        self.gotostandby = await client.post(
            f"{self.carbideEndPoint}/v1/Basic/GoToStandby", headers=self.requestHeaders
        )
    
    if self.gotostandby.status_code == 200:
        await self.actualStateName()
        while self.actualstatename.text.strip() != '"StandingBy"':
            await asyncio.sleep(1)
            await self.actualStateName()
        if self.actualstatename.text.strip() == '"StandingBy"':
            print("Laser in standby")
        else:
            print("Laser not in standby, please check state manually")
            
async def targetAttenuatorPercentage(self, percentage="0"):
    """_summary_

    Args:
        percentage (str, optional): percentage to request. Defaults to "0".
    """
    async with httpx.AsyncClient() as client:
        response_actual = await client.get(
            f"{self.carbideEndPoint}/v1/Basic/ActualAttenuatorPercentage"
        )
        if response_actual.status_code == 200:
            self.actualattenuatorpercentage_float = float(response_actual.text)
        
        response_set = await client.put(
            f"{self.carbideEndPoint}/v1/Basic/TargetAttenuatorPercentage",
            data=json.dumps(percentage),
            headers=self.requestHeaders,
        )
        
        if response_set.status_code == 200:
            response_target = await client.get(
                f"{self.carbideEndPoint}/v1/Basic/TargetAttenuatorPercentage"
            )
            if response_target.status_code == 200:
                while int(response_target.text) != int(response_actual.text):
                    print(
                        f"Target attenuator percentage is {response_target.text}, currently at {response_actual.text}"
                    )
                    response_actual = await client.get(
                        f"{self.carbideEndPoint}/v1/Basic/ActualAttenuatorPercentage"
                    )
            else:
                print("Cannot get requested attenuator percentage")
        elif response_set.status_code == 403:
            print(f"Cannot set to this value, likely out of bounds")
        else:
            print("Error setting target attenuator percentage")

async def targetPulseDuration(self, length="290"):
    """_summary_

    Args:
        length (str, optional): pulse length to request (-ve = negative chirp, otherwise positive).
        Defaults to "290".
    """
    async with httpx.AsyncClient() as client:
        response_set = await client.put(
            f"{self.carbideEndPoint}/v1/Basic/TargetPulseDuration",
            data=json.dumps(length),
            headers=self.requestHeaders,
        )
        
        if response_set.status_code == 200:
            response_target = await client.get(
                f"{self.carbideEndPoint}/v1/Basic/TargetPulseDuration"
            )
            if response_target.status_code == 200:
                response_actual = await client.get(
                    f"{self.carbideEndPoint}/v1/Basic/ActualPulseDuration"
                )
                while int(response_target.text) != int(response_actual.text):
                    print(
                        f"Target pulse duration is {response_target.text}, currently at {response_actual.text}"
                    )
                    response_actual = await client.get(
                        f"{self.carbideEndPoint}/v1/Basic/ActualPulseDuration"
                    )
            else:
                print("Cannot get requested pulse duration")
        elif response_set.status_code == 403:
            print(f"Cannot set to this value, likely out of bounds")
        else:
            print("Error setting pulse duration")
            
async def targetPpDivider(self, divider="1000"):
    async with httpx.AsyncClient() as client:
        response_set = await client.put(
            f"{self.carbideEndPoint}/v1/Basic/TargetPpDivider",
            data=json.dumps(divider),
            headers=self.requestHeaders,
        )
        if response_set.status_code == 200:
            response_get = await client.get(
                f"{self.carbideEndPoint}/v1/Basic/TargetPpDivider"
            )
            if response_get.status_code == 200:
                response_actual = await client.get(
                    f"{self.carbideEndPoint}/v1/Basic/ActualPpDivider"
                )
                while int(response_get.text) != int(response_actual.text):
                    print(
                        f"Target pulse picker divider is {response_get.text}, currently at {response_actual.text}"
                    )
                    response_actual = await client.get(
                        f"{self.carbideEndPoint}/v1/Basic/ActualPpDivider"
                    )
            else:
                print("Cannot get requested pulse duration")
        elif response_set.status_code == 403:
            print("Cannot set to this value, likely out of bounds")
        else:
            print("Error setting divider")

async def targetRaFrequency(self, frequency="60"):
    async with httpx.AsyncClient() as client:
        response_set = await client.put(
            f"{self.carbideEndPoint}/v1/Basic/TargetRaFrequency",
            data=json.dumps(frequency),
            headers=self.requestHeaders,
        )
        if response_set.status_code == 200:
            response_get = await client.get(
                f"{self.carbideEndPoint}/v1/Basic/TargetRaFrequency"
            )
            if response_get.status_code == 200:
                response_actual = await client.get(
                    f"{self.carbideEndPoint}/v1/Basic/ActualRaFrequency"
                )
                while int(response_get.text) != int(response_actual.text):
                    print(
                        f"Target RA frequency is {response_get.text}, currently at {response_actual.text}"
                    )
                    response_actual = await client.get(
                        f"{self.carbideEndPoint}/v1/Basic/ActualRaFrequency"
                    )
            else:
                print("Cannot get requested RA frequency")
        elif response_set.status_code == 403:
            print("Cannot set RA frequency to this value, likely out of bounds")
        else:
            print("Error setting RA frequency")

async def isRemoteInterlockActive(self):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{self.carbideEndPoint}/v1/Advanced/IsRemoteInterlockActive"
        )
        if response.status_code == 200:
            if response.text == "true":
                print("Remote interlock armed")
            elif response.text == "false":
                print("Remote interlock is NOT armed")
        else:
            print("Cannot get remote interlock state")

async def resetRemoteInterlock(self):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{self.carbideEndPoint}/v1/Advanced/ResetRemoteInterlock",
            headers=self.requestHeaders,
        )
        if response.status_code == 200:
            print("Remote interlock reset")
            await self.isRemoteInterlockActive()
        elif response.status_code == 403:
            print("Cannot reset remote interlock")
            await self.isRemoteInterlockActive()
        else:
            print("Error resetting remote interlock")

async def isPpEnabled(self):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{self.carbideEndPoint}/v1/Advanced/IsPpEnabled"
        )
        if response.status_code == 200:
            if response.text == "true":
                print("Pulse picker is enabled")
                self.pulsepickerstatus = True
            elif response.text == "false":
                print("Pulse picker not enabled")
                self.pulsepickerstatus = False
            else:
                print("Can't get pulse picker status")
        else:
            print("Error getting pulse picker status")

async def togglePulsePicker(self, toggle="off"):
    async with httpx.AsyncClient() as client:
        if toggle == "off":
            response = await client.post(
                f"{self.carbideEndPoint}/v1/Advanced/EnablePp",
                headers=self.requestHeaders,
            )
            if response.status_code == 200:
                print("Enabling pulse picker")
                await self.isPpEnabled()
            elif response.status_code == 403:
                print("Could not enable pulse picker")
                await self.isPpEnabled()
            else:
                print("Error enabling pulse picker")
                await self.isPpEnabled()
        elif toggle == "on":
            response = await client.post(
                f"{self.carbideEndPoint}/v1/Advanced/DisablePp",
                headers=self.requestHeaders,
            )
            if response.status_code == 200:
                print("Disabling pulse picker")
                await self.isPpEnabled()
            elif response.status_code == 403:
                print("Could not disable pulse picker (probably already disabled)")
                await self.isPpEnabled()
            else:
                print("Error disabling pulse picker")
                await self.isPpEnabled()
        else:
            print(f"Unknown request of pulse picker state: {toggle}")

async def getAomTriggerSource(self):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{self.carbideEndPoint}/v1/ExternalControl/AomTriggerSource"
        )
        if response.status_code == 200:
            print(f"AOM trigger source is set to {response.text}")
            if response.text == '"Internal"':
                self.currentaomtriggersource = 1
            elif response.text == '"ExternalLow"':
                self.currentaomtriggersource = 2
            elif response.text == '"ExternalHigh"':
                self.currentaomtriggersource = 3
            else:
                print("Unknown current trigger source")
                self.currentaomtriggersource = 0
        else:
            print("Cannot get AOM trigger source")

async def setAomTriggerSource(self, source="Internal"):
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{self.carbideEndPoint}/v1/ExternalControl/AomTriggerSource",
            data=json.dumps(source),
            headers=self.requestHeaders,
        )
        if response.status_code == 200:
            await self.getAomTriggerSource()
        elif response.status_code == 403:
            print("Could not set trigger source")
            await self.getAomTriggerSource()
        else:
            print("Error setting trigger source")

async def isPowerlockEnabled(self):
    await self.actualValues()
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{self.carbideEndPoint}/v1/Basic/IsPowerlockEnabled"
        )
        if response.status_code == 200:
            if response.text == "true":
                self.powerlockstatus = "enabled"
            elif response.text == "false":
                self.powerlockstatus = "disabled"
            print(f"Powerlock is currently {self.powerlockstatus}")

async def powerlockControl(self, state="enable"):
    async with httpx.AsyncClient() as client:
        if state == "enable":
            response = await client.post(
                f"{self.carbideEndPoint}/v1/Basic/EnablePowerlock",
                headers=self.requestHeaders,
            )
            if response.status_code == 200:
                print("Enabling powerlock...")
                while self.powerlockstatus != "enabled":
                    await asyncio.sleep(1)
                    await self.isPowerlockEnabled()
            elif response.status_code == 403:
                print("Unable to enable powerlock")
            else:
                print("Error enabling powerlock")
        elif state == "disable":
            response = await client.post(
                f"{self.carbideEndPoint}/v1/Basic/DisablePowerlock",
                headers=self.requestHeaders,
            )
            if response.status_code == 200:
                print("Disabling powerlock...")
                while self.powerlockstatus != "disabled":
                    await asyncio.sleep(1)
                    await self.isPowerlockEnabled()
            elif response.status_code == 403:
                print("Unable to disable powerlock")
            else:
                print("Error disabling powerlock")

async def reduceLeak(self):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{self.carbideEndPoint}/v1/Advanced/ReduceLeak"
        )
        if response.status_code == 200:
            print("Reducing leak...")
            await asyncio.sleep(3)
            print("Leak reduction successful")
        elif response.status_code == 403:
            print("Unable to run leak reduction")
            
async def main():
    run = carbide(endpoint="http://192.168.240.10:20010")

    # Run async functions concurrently using asyncio.gather
    await asyncio.gather(
        run.isOutputEnabled(),
        run.selectAndApplyPreset("5"),
        run.changeOutput("enable")
    )
    await asyncio.sleep(5)  # Async sleep
    await run.changeOutput()

if __name__ == "__main__":
    asyncio.run(main())