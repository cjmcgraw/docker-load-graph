#! /usr/bin/env bash
function usage() {
    echo "$0 args"
    echo ""
    echo "optional arguments:"
    echo "  --no-install  build but do not install the package"
}

install="1"

while [[ $# -gt 0 ]];do echo "$#"; case $1 in
    --no-install) no_install="";;
    --help) usage; exit 0 ;;
esac; shift; done

set -eu

python -m build


if [[ "${install}" ]]; then
    tar_to_install=$(find dist -type f -name "*.tar.gz")
    pip install ${tar_to_install}
fi
