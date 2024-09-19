Python-Accessible Functionalities via Tableau API

This document outlines the major functionalities available through Tableau’s REST API and the Tableau Server Client (TSC) library. These functions allow for extensive automation and integration of Tableau Server with Python-based workflows.

1. Authentication

	•	Authenticate to Tableau Server
	•	Sign in and authenticate to a Tableau Server or Tableau Online instance.

2. Workbooks

	•	List Workbooks
	•	Retrieve a list of all workbooks on the server, including details like name, project, and owner.
	•	Download Workbook
	•	Download a workbook (.twbx file) to a local machine.
	•	Publish Workbook
	•	Publish a new workbook to Tableau Server, either to a specific project or site.
	•	Delete Workbook
	•	Remove a workbook from Tableau Server.
	•	Refresh Workbook Extract
	•	Trigger a data extract refresh for a specific workbook.
	•	Get Workbook Connections
	•	Retrieve information about data connections used in a specific workbook.
	•	Update Workbook
	•	Update metadata or permissions of a specific workbook.

3. Data Sources

	•	List Data Sources
	•	Retrieve a list of all data sources available on the server.
	•	Publish Data Source
	•	Publish a new data source to a Tableau project.
	•	Download Data Source
	•	Download a data source (.tdsx file) to a local machine.
	•	Refresh Data Source
	•	Trigger a data refresh for a Tableau data source.
	•	Delete Data Source
	•	Remove a data source from Tableau Server.
	•	Get Data Source Connections
	•	Retrieve the connection details (e.g., database connections) for a specific data source.

4. Projects

	•	List Projects
	•	Retrieve a list of all projects on Tableau Server.
	•	Create Project
	•	Create a new project on Tableau Server.
	•	Update Project
	•	Update project details like name or permissions.
	•	Delete Project
	•	Delete a project from Tableau Server.

5. Users

	•	List Users
	•	Retrieve a list of users on Tableau Server or a specific site.
	•	Add User to Server or Site
	•	Add a new user to Tableau Server or a specific site.
	•	Update User
	•	Modify user details like username, site role, etc.
	•	Remove User
	•	Remove a user from Tableau Server or a specific site.

6. Groups

	•	List Groups
	•	Retrieve all groups in Tableau Server or a specific site.
	•	Create Group
	•	Create a new group.
	•	Delete Group
	•	Remove an existing group.
	•	Add User to Group
	•	Add a user to a group.
	•	Remove User from Group
	•	Remove a user from a group.

7. Sites

	•	List Sites
	•	Retrieve a list of all sites on Tableau Server.
	•	Create Site
	•	Create a new site on Tableau Server.
	•	Update Site
	•	Modify site details such as site name or size limits.
	•	Delete Site
	•	Delete an existing site from Tableau Server.

8. Schedules

	•	List Schedules
	•	Retrieve a list of all schedules for extract refreshes, subscriptions, or flows.
	•	Create Schedule
	•	Create a new schedule on Tableau Server (e.g., for extract refreshes or flows).
	•	Update Schedule
	•	Modify schedule details like frequency, priority, or execution time.
	•	Delete Schedule
	•	Remove a schedule from Tableau Server.

9. Tasks

	•	List Tasks
	•	Retrieve all scheduled tasks, such as extract refreshes or subscriptions.
	•	Run Extract Refresh Task
	•	Trigger an extract refresh for a specific workbook or data source.

10. Subscriptions

	•	List Subscriptions
	•	Retrieve all subscriptions on Tableau Server.
	•	Create Subscription
	•	Create a new subscription to email workbook views or dashboards to users.
	•	Delete Subscription
	•	Remove an existing subscription from Tableau Server.

11. Permissions

	•	List Permissions
	•	Retrieve permissions for a workbook, data source, or project.
	•	Add Permissions
	•	Add new permissions for a user or group to a workbook, data source, or project.
	•	Update Permissions
	•	Modify existing permissions.
	•	Delete Permissions
	•	Remove permissions for a user or group.

12. Metadata

	•	Query Metadata
	•	Query detailed metadata information about workbooks, data sources, views, and fields using Tableau’s Metadata API.
	•	Get Data Quality Warnings
	•	Retrieve data quality warnings associated with Tableau content like data sources or workbooks.

13. Extracts

	•	Create Extract
	•	Convert a live data source to an extract.
	•	Delete Extract
	•	Remove an existing extract from a workbook or data source.
	•	Get Extracts
	•	Retrieve a list of all extracts on Tableau Server.

14. Jobs

	•	List Jobs
	•	Retrieve a list of all running or completed jobs on Tableau Server.
	•	Cancel Job
	•	Cancel a running job on Tableau Server.

15. Views

	•	List Views
	•	Retrieve all views available on Tableau Server.
	•	Query View Data
	•	Query the underlying data of a specific view.
	•	Download View Image/PDF
	•	Download an image or PDF of a specific view.
	•	Favorite/Unfavorite Vie