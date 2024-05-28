# Branches API with Basic Authentication

## Overview

This is a RESTful API built with Flask that allows you to manage information about people. The API provides endpoints to:

* Retrieve a list of branches.
* Retrieve details of a specific branch by ID.
* Create new branch entries.
* Update existing branches entries.
* Delete person entries.
* Search for branch based on name or city.

The API uses Basic Authentication to secure endpoints from unauthorized access.

## Requirements

* Python 3.x
* Flask
* Flask-MySQLdb (or a similar library for database interaction)
* MySQL (or a compatible database)
* Flask-HTTPAuth (for Basic Authentication)

## Installation

1. Clone the Repository:

   ```bash
   git clone <your-repository-url>
   cd <your-repository-directory>
