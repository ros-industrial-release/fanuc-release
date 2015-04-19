Name:           ros-hydro-fanuc-m20ia10l-moveit-config
Version:        0.3.2
Release:        0%{?dist}
Summary:        ROS fanuc_m20ia10l_moveit_config package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/fanuc_m20ia10l_moveit_config
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-fanuc-m20ia-moveit-plugins
Requires:       ros-hydro-fanuc-m20ia-support
Requires:       ros-hydro-industrial-robot-simulator
Requires:       ros-hydro-joint-state-publisher
Requires:       ros-hydro-moveit-fake-controller-manager
Requires:       ros-hydro-moveit-planners-ompl
Requires:       ros-hydro-moveit-ros-move-group
Requires:       ros-hydro-moveit-ros-visualization
Requires:       ros-hydro-moveit-simple-controller-manager
Requires:       ros-hydro-robot-state-publisher
Requires:       ros-hydro-xacro
BuildRequires:  ros-hydro-catkin

%description
MoveIt package for the Fanuc M-20iA/10L. An automatically generated package
with all the configuration and launch files for using the Fanuc M-20iA/10L with
the MoveIt Motion Planning Framework. NB: this package currently uses the
default MoveIt acceleration limits (ie: 1/5th of joint velocity limits), instead
of the true acceleration limits for this manipulator (see issue 49).

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
* Sun Apr 19 2015 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.3.2-0
- Autogenerated by Bloom

* Wed Jan 21 2015 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.3.1-0
- Autogenerated by Bloom

* Thu Jan 08 2015 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.3.0-0
- Autogenerated by Bloom

