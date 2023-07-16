# Odoo HR Extend (hr_extend)

This module adds some variables to hr_employee.

### employee_no
    it will be used as employee number which is used in many companies.
    hr -> employee -> hr settings
###  card_no
    It is a number which in some companies is the same as employee_no. It is a number
        which is setup on biometric access control systems.
    hr -> employee -> hr settings

###  personal_email
    It is added to use for sending email to some employees the special reports.
        One of the reports is the present on a building report.
    hr -> employee -> personal information

    If it is set for someone and the employee is added to the following record,
        he or she can receive presents of the building report.
    Service Desk -> settings -> reports ; record:recipients

### Change log
0.1.6
    loaded on gilaneh

15.1.5
Prepared for git push.

0.1.4
Added hr.employee.public class as a workaround for user rights



