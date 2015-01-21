Name:           ros-hydro-fanuc-m430ia-support
Version:        0.3.1
Release:        0%{?dist}
Summary:        ROS fanuc_m430ia_support package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/fanuc_m430ia_support
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-fanuc-driver
Requires:       ros-hydro-fanuc-resources
Requires:       ros-hydro-joint-state-publisher
Requires:       ros-hydro-robot-state-publisher
Requires:       ros-hydro-rviz
Requires:       ros-hydro-xacro
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-roslaunch >= 1.9.55

%description
ROS-Industrial support for the Fanuc M-430iA (and variants). This package
contains configuration data, 3D models and launch files for Fanuc M-430iA
manipulators. This currently includes the /2F and /2P. Specifications:
M-430iA/2F - &quot;Default J1 range&quot; M-430iA/2P - &quot;Default J1
range&quot; Joint limits and maximum joint velocities are based on the
information in the FANUC Robot M-430iA Mechanical Unit Operator's Manual version
B-82554EN/05. All urdfs are based on the default motion and joint velocity
limits, unless noted otherwise (ie: no support for high speed joints, extended /
limited motion ranges or other options). Before using any of the configuration
files and / or meshes included in this package, be sure to check they are
correct for the particular robot model and configuration you intend to use them
with.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Jan 21 2015 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.3.1-0
- Autogenerated by Bloom

* Thu Jan 08 2015 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.3.0-0
- Autogenerated by Bloom

