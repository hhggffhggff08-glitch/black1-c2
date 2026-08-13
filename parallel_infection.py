import threading

class ParallelInfection:
    def __init__(self):
        self.devices = []
        self.infection_threads = []

    def infect_parallel(self):
        """إصابة متوازية لكل الأجهزة"""
        print("⚡ Parallel infection of all devices...")
        for device in self.devices:
            thread = threading.Thread(target=self.infect_device, args=(device,))
            self.infection_threads.append(thread)
            thread.start()
        for thread in self.infection_threads:
            thread.join()
        print("💀 All devices infected in parallel")
        return True

    def infect_device(self, device):
        """إصابة جهاز معين"""
        print(f"⚡ Infecting {device} in parallel...")
        self.install_script(device)
        self.activate_ghost(device)
        return True

    def install_script(self, device):
        """تثبيت الأسكربت"""
        print(f"📥 Installing on {device}...")
        return True

    def activate_ghost(self, device):
        """تفعيل وضع الشبح"""
        print(f"👻 Ghost mode on {device}...")
        return True