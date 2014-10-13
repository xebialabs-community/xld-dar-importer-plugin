# Preface #

This document describes the functionality provided by the dar importer plugin.

See the **XL Deploy Reference Manual** for background information on XL Deploy and deployment concepts.

# Overview #

The dar importer plugin is a XL Deploy plugin that adds capability for searching and importing dar files from a Nexus repo.

# Requirements #

* **Requirements**
	* **XL Deploy** 4.5.0

# Installation #

Place the plugin JAR file into your `SERVER_HOME/plugins` directory.

# Usage #

1. Go to `Repository - Configuration`, create a new `repository.Importer`.
   For example: 
   kind: nexus
   server url: http://nexus.xebialabs.com/nexus/service/local
2. Go to the `Import` ui extension and select the repository you want the search
3. Type the artifact id you want to search for, and select one of the suggestions.
4. Click on import.
