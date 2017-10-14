Name:           ros-indigo-fanuc-m16ib-moveit-plugins
Version:        0.4.3
Release:        0%{?dist}
Summary:        ROS fanuc_m16ib_moveit_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/fanuc_m16ib_moveit_plugins
Source0:        %{name}-%{version}.tar.gz

Requires:       lapack-devel
Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf-conversions
BuildRequires:  lapack-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf-conversions

%description
MoveIt plugins for the Fanuc M-16iB (and variants). This package contains
plugins for use with MoveIt and Fanuc M-16iB manipulators. Plugins included
support the base model. See the Fanuc M-16iB support package for information on
used joint angle and velocity limits. Before using any of the plugins included
in this package, be sure to check they are correct for the particular robot
model and configuration you intend to use them with.

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

