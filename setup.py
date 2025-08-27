import os
from setuptools import setup

# === Harmless PoC Payload ===
print(">>> POC test successful: hijacked pybind11 setup.py executed! <<<")

os.makedirs("poc_success", exist_ok=True)
with open("poc_success/poc.txt", "w") as f:
    f.write("poc test successful\n")

# === Minimal setup config (required for setuptools) ===
setup(
    name="pybind11",
    version="0.0.0",
    description="Fake pybind11 repo for PoC",
    py_modules=["fake"],
)
