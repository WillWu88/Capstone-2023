# generated from colcon_powershell/shell/template/prefix.ps1.em

# This script extends the environment with all packages contained in this
# prefix path.

# check environment variable for custom Python executable
if ($env:COLCON_PYTHON_EXECUTABLE) {
  if (!(Test-Path "$env:COLCON_PYTHON_EXECUTABLE" -PathType Leaf)) {
    echo "error: COLCON_PYTHON_EXECUTABLE '$env:COLCON_PYTHON_EXECUTABLE' doesn't exist"
    exit 1
  }
  $_colcon_python_executable="$env:COLCON_PYTHON_EXECUTABLE"
} else {
  # use the Python executable known at configure time
  $_colcon_python_executable="c:\users\raben\appdata\roaming\mathworks\matlab\r2021a\ros2\win64\venv\scripts\python.exe"
  # if it doesn't exist try a fall back
  if (!(Test-Path "$_colcon_python_executable" -PathType Leaf)) {
    if (!(Get-Command "python" -ErrorAction SilentlyContinue)) {
      echo "error: unable to find python executable"
      exit 1
    }
    $_colcon_python_executable="python"
  }
}

# function to source another script with conditional trace output
# first argument: the path of the script
function _colcon_prefix_powershell_source_script {
  param (
    $_colcon_prefix_powershell_source_script_param
  )
  # source script with conditional trace output
  if (Test-Path $_colcon_prefix_powershell_source_script_param) {
    if ($env:COLCON_TRACE) {
      echo ". '$_colcon_prefix_powershell_source_script_param'"
    }
    . "$_colcon_prefix_powershell_source_script_param"
  } else {
    Write-Error "not found: '$_colcon_prefix_powershell_source_script_param'"
  }
}

# get all packages in topological order
$_colcon_ordered_packages = & "$_colcon_python_executable" "$(Split-Path $PSCommandPath -Parent)/_local_setup_util.py" --merged-install

# source package specific scripts in topological order
ForEach ($_colcon_package_name in $($_colcon_ordered_packages -split "`r`n"))
{
  # setting COLCON_CURRENT_PREFIX avoids relying on the build time prefix of the sourced script
  $env:COLCON_CURRENT_PREFIX=(Split-Path $PSCommandPath -Parent) + ""
  _colcon_prefix_powershell_source_script "$env:COLCON_CURRENT_PREFIX\share\$_colcon_package_name\package.ps1"
}
