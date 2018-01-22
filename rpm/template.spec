Name:           ros-indigo-fanuc
Version:        0.4.4
Release:        0%{?dist}
Summary:        ROS fanuc package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/fanuc
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-fanuc-driver
Requires:       ros-indigo-fanuc-lrmate200ib-moveit-config
Requires:       ros-indigo-fanuc-lrmate200ib-moveit-plugins
Requires:       ros-indigo-fanuc-lrmate200ib-support
Requires:       ros-indigo-fanuc-lrmate200ib3l-moveit-config
Requires:       ros-indigo-fanuc-lrmate200ic-moveit-config
Requires:       ros-indigo-fanuc-lrmate200ic-moveit-plugins
Requires:       ros-indigo-fanuc-lrmate200ic-support
Requires:       ros-indigo-fanuc-lrmate200ic5h-moveit-config
Requires:       ros-indigo-fanuc-lrmate200ic5l-moveit-config
Requires:       ros-indigo-fanuc-m10ia-moveit-config
Requires:       ros-indigo-fanuc-m10ia-moveit-plugins
Requires:       ros-indigo-fanuc-m10ia-support
Requires:       ros-indigo-fanuc-m16ib-moveit-plugins
Requires:       ros-indigo-fanuc-m16ib-support
Requires:       ros-indigo-fanuc-m16ib20-moveit-config
Requires:       ros-indigo-fanuc-m20ia-moveit-config
Requires:       ros-indigo-fanuc-m20ia-moveit-plugins
Requires:       ros-indigo-fanuc-m20ia-support
Requires:       ros-indigo-fanuc-m20ia10l-moveit-config
Requires:       ros-indigo-fanuc-m430ia-moveit-plugins
Requires:       ros-indigo-fanuc-m430ia-support
Requires:       ros-indigo-fanuc-m430ia2f-moveit-config
Requires:       ros-indigo-fanuc-m430ia2p-moveit-config
Requires:       ros-indigo-fanuc-m6ib-moveit-config
Requires:       ros-indigo-fanuc-m6ib-moveit-plugins
Requires:       ros-indigo-fanuc-m6ib-support
Requires:       ros-indigo-fanuc-resources
BuildRequires:  ros-indigo-catkin

%description
ROS-Industrial support for Fanuc manipulators (metapackage).

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

