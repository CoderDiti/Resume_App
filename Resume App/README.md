#tables in Resume APP

User
    -id
    -username

PersonalDetails
    -id
    -name
    -phone
    -email
    -address
    -linkedIn
    -ForeignKey('user.id')

Projects
    -id
    -name
    -desc
    -stat_date
    -end_date
    -ForeignKey('user.id')  

Experiences
    -id
    -company_name
    -role
    -role_desc
    -start_date
    -end_date
    -ForeignKey('user.id')

Education
    -id
    -school_name
    -degree_Nme
    -start_date
    -end_date
    -ForeignKey('user.id')

Certificates
    -id
    -title
    -start_date
    -end_date
    -ForeignKey('user.id') 

Skills
    -id
    -title
    -confidence_score
    -ForeignKey('user.id')