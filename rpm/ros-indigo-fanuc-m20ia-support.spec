Name:           ros-indigo-fanuc-m20ia-support
Version:        0.4.4
Release:        0%{?dist}
Summary:        ROS fanuc_m20ia_support package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/fanuc_m20ia_support
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-fanuc-driver
Requires:       ros-indigo-fanuc-resources
Requires:       ros-indigo-joint-state-publisher
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-rviz
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch >= 1.9.55

%description
ROS-Industrial support for the Fanuc M-20iA / ARC Mate 120iC (and variants).
This package contains configuration data, 3D models and launch files for Fanuc
M-20iA / ARC Mate 120iC manipulators. This currently includes the base model and
/10L. Specifications: M-20iA - &quot;Cable integrated J3 Arm&quot; M-20iA/10L -
&quot;Cable integrated J3 Arm&quot; Joint limits and maximum joint velocities
are based on the information in the FANUC Robot ARC Mate 120iC, FANUC Robot
M-20iA Mechanical Unit Operator's Manual version B-82874EN/06. All urdfs are
based on the default motion and joint velocity limits, unless noted otherwise
(ie: no support for high speed joints, extended / limited motion ranges or other
options). Before using any of the configuration files and / or meshes included
in this package, be sure to check they are correct for the particular robot
model and configuration you intend to use them with. Contributors: This support
package has received contributions from: Joe Spanier (M-20iA/10L).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jan 22 2018 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.4.4-0
- Autogenerated by Bloom

* Sat Oct 14 2017 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.4.3-0
- Autogenerated by Bloom

* Mon May 22 2017 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.4.2-0
- Autogenerated by Bloom

* Fri Jun 17 2016 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.4.1-0
- Autogenerated by Bloom

* Tue Oct 13 2015 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.4.0-1
- Autogenerated by Bloom

* Sun Oct 11 2015 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.4.0-0
- Autogenerated by Bloom
