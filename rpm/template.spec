Name:           ros-indigo-fanuc-m10ia-support
Version:        0.4.2
Release:        0%{?dist}
Summary:        ROS fanuc_m10ia_support package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/fanuc_m10ia_support
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
ROS-Industrial support for the Fanuc M-10iA (and variants). This package
contains configuration data, 3D models and launch files for Fanuc M-10iA
manipulators. This includes the base model and the /7L variant. Specifications:
M-10iA - &quot;Conventional dress-out&quot; M-10iA/7L - &quot;Conventional
dress-out&quot; Joint limits and maximum joint velocities are based on the
information in the FANUC Robot M-10iA Mechanical Unit Operator's Manual version
B-82754EN/09. All urdfs are based on the default motion and joint velocity
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
* Mon May 22 2017 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.4.2-0
- Autogenerated by Bloom

* Fri Jun 17 2016 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.4.1-0
- Autogenerated by Bloom

* Tue Oct 13 2015 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.4.0-1
- Autogenerated by Bloom

* Sun Oct 11 2015 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.4.0-0
- Autogenerated by Bloom

