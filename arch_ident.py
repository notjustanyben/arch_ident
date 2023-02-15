import subprocess

arm_arch = "aarch64"
arm_arch2 = "ARM64"
intel_arch = "x86"

def is_arm():
    arch = subprocess.check_output(["uname -a"], shell=True, encoding="utf-8")
    if str(arm_arch) or str(arm_arch2) in arch:
        return True
    else:
        return False

def is_intel():
    arch = subprocess.check_output(["uname -a"], shell=True, encoding="utf-8")
    if str(intel_arch) in arch and arm_arch and arm_arch2 not in arch:
        return True
    else:
        return False

if is_arm():
    print("\naarch64/ARM64 Architecture found!\n")

if is_intel():
    print("\nx86/Intel Architecture found!\n")
