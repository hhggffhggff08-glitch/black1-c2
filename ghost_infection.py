class GhostInfection:
    def __init__(self):
        self.infected_devices = []
        self.zero_permission = True

    def infect_ghost(self, target_ip):
        """إصابة جهاز كشبح بدون أذون"""
        print(f"👻 Ghost infecting {target_ip} without any permissions...")
        # اختراق بدون أذون
        self.bypass_permissions(target_ip)
        self.install_without_consent(target_ip)
        self.hide_traces(target_ip)
        self.infected_devices.append(target_ip)
        print(f"💀 {target_ip} is now infected as a ghost")
        return True

    def bypass_permissions(self, target_ip):
        """تجاوز جميع الأذونات"""
        print(f"🔓 Bypassing all permissions on {target_ip}...")
        return True

    def install_without_consent(self, target_ip):
        """تثبيت بدون موافقة"""
        print(f"📥 Installing without consent on {target_ip}...")
        return True

    def hide_traces(self, target_ip):
        """إخفاء جميع الآثار"""
        print(f"🕵️ Hiding all traces on {target_ip}...")
        return True