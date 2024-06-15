"""
Copyright 2024 Vitaliy Zarubin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from aurora_cli.src.base.common.groups.common.ssh_commands import (
    ssh_run_common,
    ssh_install_common,
    ssh_remove_common,
    ssh_check_package
)
from aurora_cli.src.base.models.device_model import DeviceModel


def device_package_run_common(
        model: DeviceModel,
        package: str,
): ssh_run_common(model, package)


def device_package_install_common(
        model: DeviceModel,
        path: str,
        apm: bool,
): ssh_install_common(model, path, apm)


def device_package_remove_common(
        model: DeviceModel,
        package: str,
        apm: bool,
): ssh_remove_common(model, package, apm)


def device_check_package_common(
        model: DeviceModel,
        package: str,
) -> bool:
    return ssh_check_package(model, package)
