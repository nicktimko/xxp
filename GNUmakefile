# Makefile for auth Service

SHELL := bash
.ONESHELL:
.SHELLFLAGS := -o errexit -o nounset -o pipefail -c
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

python_version := 3.10
venv_target := venv
venv_dir := .venv

${venv_target}: test-requirements.txt
	if [ -d "${venv_dir}" ]; then
		# kinda hacky, but can be much faster than the full rebuild
		${venv_dir}/bin/pip install pip-tools
		${venv_dir}/bin/pip-sync
		${venv_dir}/bin/pip uninstall -y pip-tools
	else
		rm -rf "${venv_dir}"
		python${python_version} -m venv ${venv_dir}
		${venv_dir}/bin/python -m pip install \
			--disable-pip-version-check \
			--requirement $<
		${venv_dir}/bin/python -m pip list > ${venv_target}
	fi
	${venv_dir}/bin/python -m pip install -e .
