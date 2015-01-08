Name:           ros-hydro-fanuc-m10ia-moveit-plugins
Version:        0.3.0
Release:        0%{?dist}
Summary:        ROS fanuc_m10ia_moveit_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/fanuc_m10ia_moveit_plugins
Source0:        %{name}-%{version}.tar.gz

Requires:       lapack-devel
Requires:       ros-hydro-moveit-core
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-tf-conversions
BuildRequires:  lapack-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-moveit-core
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-tf-conversions

%description
MoveIt plugins for the Fanuc M-10iA (and variants). This package contains
plugins for use with MoveIt and Fanuc M-10iA manipulators. Plugins included
support the base model. See the Fanuc M-10iA support package for information on
used joint angle and velocity limits. Before using any of the plugins included
in this package, be sure to check they are correct for the particular robot
model and configuration you intend to use them with.

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
* Thu Jan 08 2015 G.A. vd. Hoorn (TU Delft Robotics Institute) <g.a.vanderhoorn@tudelft.nl> - 0.3.0-0
- Autogenerated by Bloom

