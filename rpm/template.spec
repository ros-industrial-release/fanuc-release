Name:           ros-indigo-fanuc-resources
Version:        0.4.1
Release:        0%{?dist}
Summary:        ROS fanuc_resources package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/fanuc_resources
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  ros-indigo-catkin

%description
Shared configuration data, 3D models and launch files for Fanuc manipulators.
This package contains configuration data, 3D models and launch files that are
shared between different Fanuc robot support packages within the ROS-Industrial
program. This package also contains common urdf / xacro resources used by other
Fanuc related packages.

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
* Fri Jun 17 2016 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.4.1-0
- Autogenerated by Bloom

* Tue Oct 13 2015 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.4.0-1
- Autogenerated by Bloom

* Sun Oct 11 2015 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.4.0-0
- Autogenerated by Bloom

