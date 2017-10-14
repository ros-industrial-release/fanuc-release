Name:           ros-indigo-fanuc-m430ia2p-moveit-config
Version:        0.4.3
Release:        0%{?dist}
Summary:        ROS fanuc_m430ia2p_moveit_config package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/fanuc_m430ia2p_moveit_config
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-fanuc-m430ia-moveit-plugins
Requires:       ros-indigo-fanuc-m430ia-support
Requires:       ros-indigo-industrial-robot-simulator
Requires:       ros-indigo-joint-state-publisher
Requires:       ros-indigo-moveit-fake-controller-manager
Requires:       ros-indigo-moveit-planners-ompl
Requires:       ros-indigo-moveit-ros-move-group
Requires:       ros-indigo-moveit-ros-visualization
Requires:       ros-indigo-moveit-ros-warehouse
Requires:       ros-indigo-moveit-simple-controller-manager
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-rviz
Requires:       ros-indigo-warehouse-ros
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch

%description
MoveIt package for the Fanuc M-430iA/2P. An automatically generated package
with all the configuration and launch files for using the Fanuc M-430iA/2P with
the MoveIt Motion Planning Framework. NB: this package currently uses the
default MoveIt acceleration limits (ie: 1/5th of joint velocity limits), instead
of the true acceleration limits for this manipulator (see issue 49).

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

