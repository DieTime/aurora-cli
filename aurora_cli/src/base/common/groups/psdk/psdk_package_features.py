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

from aurora_cli.src.base.common.features.shell_features import (
    shell_psdk_resign,
    shell_psdk_package_search,
    shell_psdk_package_install,
    shell_psdk_package_validate,
    shell_psdk_package_remove,
)
from aurora_cli.src.base.common.groups.psdk.__tools import psdk_tool_get_open_keys
from aurora_cli.src.base.models.psdk_model import PsdkModel
from aurora_cli.src.base.models.sign_model import SignModel
from aurora_cli.src.base.texts.info import TextInfo
from aurora_cli.src.base.utils.output import echo_stdout, OutResultInfo


def psdk_package_search_common(
        model: PsdkModel,
        target: str,
        package: str,
        verbose: bool
):
    result = shell_psdk_package_search(model.get_tool_path(), target, package)
    echo_stdout(result, verbose)


def psdk_package_install_common(
        model: PsdkModel,
        target: str,
        path: str,
        verbose: bool
):
    result = shell_psdk_package_install(model.get_tool_path(), target, path)
    echo_stdout(result, verbose)


def psdk_package_remove_common(
        model: PsdkModel,
        target: str,
        package: str,
        verbose: bool
):
    result = shell_psdk_package_remove(model.get_tool_path(), target, package)
    echo_stdout(result, verbose)


def psdk_package_validate_common(
        model: PsdkModel,
        target: str,
        path: str,
        profile: str,
        verbose: bool
):
    result = shell_psdk_package_validate(model.get_tool_path(), target, path, profile)
    echo_stdout(result, verbose)


def psdk_package_sign_common(
        model_psdk: PsdkModel,
        model_keys: SignModel | None,
        path: str,
        verbose: bool,
        is_bar: bool = True
):
    if not model_keys:
        echo_stdout(OutResultInfo(TextInfo.psdk_sign_use_public_keys()))
        keys = psdk_tool_get_open_keys(verbose, is_bar)
        model_keys = SignModel('_', keys[0], keys[1])

    result = shell_psdk_resign(
        tool=model_psdk.get_tool_path(),
        key=str(model_keys.key),
        cert=str(model_keys.cert),
        path=path
    )

    echo_stdout(result, verbose)