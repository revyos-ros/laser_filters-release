%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-laser-filters
Version:        2.0.6
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS laser_filters package

License:        BSD
URL:            http://ros.org/wiki/laser_filters
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-angles
Requires:       ros-humble-filters
Requires:       ros-humble-laser-geometry
Requires:       ros-humble-message-filters
Requires:       ros-humble-pluginlib
Requires:       ros-humble-rclcpp
Requires:       ros-humble-rclcpp-lifecycle
Requires:       ros-humble-sensor-msgs
Requires:       ros-humble-tf2
Requires:       ros-humble-tf2-ros
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake-auto
BuildRequires:  ros-humble-angles
BuildRequires:  ros-humble-filters
BuildRequires:  ros-humble-laser-geometry
BuildRequires:  ros-humble-message-filters
BuildRequires:  ros-humble-pluginlib
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-rclcpp-lifecycle
BuildRequires:  ros-humble-sensor-msgs
BuildRequires:  ros-humble-tf2
BuildRequires:  ros-humble-tf2-ros
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-gtest
%endif

%description
Assorted filters designed to operate on 2D planar laser scanners, which use the
sensor_msgs/LaserScan type.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Sat Mar 18 2023 Jon Binney <jon.binney@gmail.com> - 2.0.6-1
- Autogenerated by Bloom

* Thu May 26 2022 Jon Binney <jon.binney@gmail.com> - 2.0.5-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Jon Binney <jon.binney@gmail.com> - 2.0.4-5
- Autogenerated by Bloom

* Mon Apr 11 2022 Jon Binney <jon.binney@gmail.com> - 2.0.4-4
- Autogenerated by Bloom

* Mon Apr 11 2022 Jon Binney <jon.binney@gmail.com> - 2.0.4-3
- Autogenerated by Bloom

* Mon Apr 11 2022 Jon Binney <jon.binney@gmail.com> - 2.0.4-2
- Autogenerated by Bloom

* Mon Apr 11 2022 Jon Binney <jon.binney@gmail.com> - 2.0.4-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Jon Binney <jon.binney@gmail.com> - 2.0.1-2
- Autogenerated by Bloom

