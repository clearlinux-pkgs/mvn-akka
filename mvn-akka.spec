#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-akka
Version  : 2.6.0.m2
Release  : 2
URL      : https://github.com/akka/akka/archive/v2.6.0-M2.tar.gz
Source0  : https://github.com/akka/akka/archive/v2.6.0-M2.tar.gz
Source1  : https://repo.maven.apache.org/maven2/com/typesafe/akka/akka-testkit_2.11/2.4.20/akka-testkit_2.11-2.4.20.jar
Source2  : https://repo.maven.apache.org/maven2/com/typesafe/akka/akka-testkit_2.11/2.4.20/akka-testkit_2.11-2.4.20.pom
Source3  : https://repo1.maven.org/maven2/com/typesafe/akka/akka-actor_2.11/2.4.20/akka-actor_2.11-2.4.20.jar
Source4  : https://repo1.maven.org/maven2/com/typesafe/akka/akka-actor_2.11/2.4.20/akka-actor_2.11-2.4.20.pom
Source5  : https://repo1.maven.org/maven2/com/typesafe/akka/akka-protobuf_2.11/2.4.20/akka-protobuf_2.11-2.4.20.jar
Source6  : https://repo1.maven.org/maven2/com/typesafe/akka/akka-protobuf_2.11/2.4.20/akka-protobuf_2.11-2.4.20.pom
Source7  : https://repo1.maven.org/maven2/com/typesafe/akka/akka-remote_2.11/2.4.20/akka-remote_2.11-2.4.20.jar
Source8  : https://repo1.maven.org/maven2/com/typesafe/akka/akka-remote_2.11/2.4.20/akka-remote_2.11-2.4.20.pom
Source9  : https://repo1.maven.org/maven2/com/typesafe/akka/akka-slf4j_2.11/2.4.20/akka-slf4j_2.11-2.4.20.jar
Source10  : https://repo1.maven.org/maven2/com/typesafe/akka/akka-slf4j_2.11/2.4.20/akka-slf4j_2.11-2.4.20.pom
Source11  : https://repo1.maven.org/maven2/com/typesafe/akka/akka-stream_2.11/2.4.20/akka-stream_2.11-2.4.20.jar
Source12  : https://repo1.maven.org/maven2/com/typesafe/akka/akka-stream_2.11/2.4.20/akka-stream_2.11-2.4.20.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: mvn-akka-data = %{version}-%{release}
Requires: mvn-akka-license = %{version}-%{release}

%description
Akka [![Latest version](https://index.scala-lang.org/akka/akka/akka-actor/latest.svg)](https://index.scala-lang.org/akka/akka/akka-actor)[![Build Status](https://travis-ci.org/akka/akka.svg?branch=master)](https://travis-ci.org/akka/akka)
====

%package data
Summary: data components for the mvn-akka package.
Group: Data

%description data
data components for the mvn-akka package.


%package license
Summary: license components for the mvn-akka package.
Group: Default

%description license
license components for the mvn-akka package.


%prep
%setup -q -n akka-2.6.0-M2

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-akka
cp COPYING.protobuf %{buildroot}/usr/share/package-licenses/mvn-akka/COPYING.protobuf
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-akka/LICENSE
cp akka-docs/src/main/paradox/project/licenses.md %{buildroot}/usr/share/package-licenses/mvn-akka/akka-docs_src_main_paradox_project_licenses.md
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-testkit_2.11/2.4.20
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-testkit_2.11/2.4.20/akka-testkit_2.11-2.4.20.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-testkit_2.11/2.4.20
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-testkit_2.11/2.4.20/akka-testkit_2.11-2.4.20.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-actor_2.11/2.4.20
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-actor_2.11/2.4.20/akka-actor_2.11-2.4.20.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-actor_2.11/2.4.20
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-actor_2.11/2.4.20/akka-actor_2.11-2.4.20.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-protobuf_2.11/2.4.20
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-protobuf_2.11/2.4.20/akka-protobuf_2.11-2.4.20.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-protobuf_2.11/2.4.20
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-protobuf_2.11/2.4.20/akka-protobuf_2.11-2.4.20.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-remote_2.11/2.4.20
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-remote_2.11/2.4.20/akka-remote_2.11-2.4.20.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-remote_2.11/2.4.20
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-remote_2.11/2.4.20/akka-remote_2.11-2.4.20.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-slf4j_2.11/2.4.20
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-slf4j_2.11/2.4.20/akka-slf4j_2.11-2.4.20.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-slf4j_2.11/2.4.20
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-slf4j_2.11/2.4.20/akka-slf4j_2.11-2.4.20.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-stream_2.11/2.4.20
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-stream_2.11/2.4.20/akka-stream_2.11-2.4.20.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-stream_2.11/2.4.20
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/akka/akka-stream_2.11/2.4.20/akka-stream_2.11-2.4.20.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/typesafe/akka/akka-actor_2.11/2.4.20/akka-actor_2.11-2.4.20.jar
/usr/share/java/.m2/repository/com/typesafe/akka/akka-actor_2.11/2.4.20/akka-actor_2.11-2.4.20.pom
/usr/share/java/.m2/repository/com/typesafe/akka/akka-protobuf_2.11/2.4.20/akka-protobuf_2.11-2.4.20.jar
/usr/share/java/.m2/repository/com/typesafe/akka/akka-protobuf_2.11/2.4.20/akka-protobuf_2.11-2.4.20.pom
/usr/share/java/.m2/repository/com/typesafe/akka/akka-remote_2.11/2.4.20/akka-remote_2.11-2.4.20.jar
/usr/share/java/.m2/repository/com/typesafe/akka/akka-remote_2.11/2.4.20/akka-remote_2.11-2.4.20.pom
/usr/share/java/.m2/repository/com/typesafe/akka/akka-slf4j_2.11/2.4.20/akka-slf4j_2.11-2.4.20.jar
/usr/share/java/.m2/repository/com/typesafe/akka/akka-slf4j_2.11/2.4.20/akka-slf4j_2.11-2.4.20.pom
/usr/share/java/.m2/repository/com/typesafe/akka/akka-stream_2.11/2.4.20/akka-stream_2.11-2.4.20.jar
/usr/share/java/.m2/repository/com/typesafe/akka/akka-stream_2.11/2.4.20/akka-stream_2.11-2.4.20.pom
/usr/share/java/.m2/repository/com/typesafe/akka/akka-testkit_2.11/2.4.20/akka-testkit_2.11-2.4.20.jar
/usr/share/java/.m2/repository/com/typesafe/akka/akka-testkit_2.11/2.4.20/akka-testkit_2.11-2.4.20.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-akka/COPYING.protobuf
/usr/share/package-licenses/mvn-akka/LICENSE
/usr/share/package-licenses/mvn-akka/akka-docs_src_main_paradox_project_licenses.md
