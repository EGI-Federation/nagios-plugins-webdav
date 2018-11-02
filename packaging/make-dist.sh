#!/usr/bin/env bash
set -e

#-------------------------------------------------------------------------------
# Generate a release tarball - run this from the root of the git repository.
#-------------------------------------------------------------------------------
git submodule update --recursive --init
mkdir -p build

#-------------------------------------------------------------------------------
# Extract version number, we need this for the archive name
#-------------------------------------------------------------------------------
VERSION_FULL=$(grep '__version__ = ' ./src/check_webdav | cut -d '"' -f2)
printf "Version: ${VERSION_FULL}\n"
FILENAME="nagios-plugins-webdav-${VERSION_FULL}"

#-------------------------------------------------------------------------------
# Make the archive
#-------------------------------------------------------------------------------
TARGET_PATH=$(basename "$PWD")

pushd "$PWD"/..
tar --exclude '*/.git' --exclude "${TARGET_PATH}/build" -pcvzf "${TARGET_PATH}/build/${FILENAME}.tar.gz" "${TARGET_PATH}" --transform "s!^${TARGET_PATH}!${FILENAME}!" --show-transformed-names
popd
