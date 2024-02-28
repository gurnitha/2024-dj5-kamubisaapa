# ////////////////////////// ori ////////////////////////////

mysql> desc projects_project;
+-------------+---------------+------+-----+---------+-------+
| Field       | Type          | Null | Key | Default | Extra |
+-------------+---------------+------+-----+---------+-------+
| title       | varchar(200)  | NO   |     | NULL    |       |
| description | longtext      | YES  |     | NULL    |       |
| demo_link   | varchar(2000) | YES  |     | NULL    |       |
| source_link | varchar(2000) | YES  |     | NULL    |       |
| created     | datetime(6)   | NO   |     | NULL    |       |
| id          | char(32)      | NO   | PRI | NULL    |       |
| vote_ratio  | int(11)       | YES  |     | NULL    |       |
| vote_total  | int(11)       | YES  |     | NULL    |       |
+-------------+---------------+------+-----+---------+-------+
8 rows in set (0.00 sec)

mysql> select * from projects_project;
+-----------+-----------------------+-----------+-------------+----------------------------+----------------------------------+------------+------------+
| title     | description           | demo_link | source_link | created                    | id                               | vote_ratio | vote_total |
+-----------+-----------------------+-----------+-------------+----------------------------+----------------------------------+------------+------------+
| Project 1 | Project 1 description | NULL      | NULL        | 2021-10-17 12:39:56.327543 | 13d7d7329a6d4b3eb1bf40c51f1cac86 |         67 |        123 |
| Project 3 | Project 3 description | NULL      | NULL        | 2021-10-17 12:40:47.140889 | 488bbab1457b4e3887bce54e3d01a3c8 |         68 |         24 |
| Project 4 | Project 4 description | NULL      | NULL        | 2021-10-17 12:41:33.200415 | 979fb56014ae497b908246d6ee5f3939 |         88 |        120 |
| Project 5 | Project 5 description | NULL      | NULL        | 2021-10-17 12:42:00.038770 | d9d1a7b2caf5459aabb884b0e52c40c0 |         89 |        234 |
| Project 2 | Project 2 description | NULL      | NULL        | 2021-10-17 12:40:19.666157 | e490873bb23b4182a6d69cacf765d534 |         50 |         34 |
+-----------+-----------------------+-----------+-------------+----------------------------+----------------------------------+------------+------------+
5 rows in set (0.00 sec)


### select title from projects_project;

### DJANGO QUERYSET

In [1]: from projects.models import Project                                                            
                                                                                                       
In [2]: projects = Project.objects.all()                                                               
                                                                                                       
In [3]: print(projects)                                                                                
<QuerySet [
    <Project: Project 1>, 
    <Project: Project 3>, 
    <Project: Project 4>, 
    <Project: Project 5>, 
    <Project: Project 2>]>                                                                                     

### SQL

mysql> select title from projects_project;
+-----------+
| title     |
+-----------+
| Project 1 |
| Project 3 |
| Project 4 |
| Project 5 |
| Project 2 |
+-----------+
5 rows in set (0.00 sec)                                                                                          

### select title from projects_project where title="Project 1";                                                                                           

### DJANGO QUERYSET

In [1]: from projects.models import Project                                                            
                                                                                             
In [2]: obj = Project.objects.get(title="Project 1")                                                   
                                                                                                       
In [3]: print(obj)                                                                                     
Project 1                                                                                              
                                                                                                       
In [4]: print(obj.title)                                                                               
Project 1                                                                                              

### SQL

mysql> select title from projects_project where title="Project 1";
+-----------+
| title     |
+-----------+
| Project 1 |
+-----------+
1 row in set (0.00 sec)


### select created from projects_project where created="2021-10-17 12:39:56.327543";

### DJANGO QUERYSET
                  
In [1]: from projects.models import Project                                                            
                                                                                             
In [2]: obj = Project.objects.get(title="Project 1")                                                   
                                                                                                       
In [3]: print(obj)                                                                                     
Project 1                                                                                              
                                                                                                       
In [4]: print(obj.title)                                                                               
Project 1 

In [5]: print(obj.created)                                                                             
2021-10-17 12:39:56.327543+00:00                                                                       

### SQL

mysql> select created from projects_project where created="2021-10-17 12:39:56.327543";
+----------------------------+
| created                    |
+----------------------------+
| 2021-10-17 12:39:56.327543 |
+----------------------------+
1 row in set (0.00 sec)
                                      
                                                                                                       

### INNER JOIN - projects_project table and projects_review table
###            - OneToMany relationship

### DJANGO QUERYSET
                  
In [1]: from projects.models import Project                                                            
                                                                                             
In [2]: obj = Project.objects.get(title="Project 1")                                                   
                                                                                                       
In [3]: print(obj)                                                                                     
Project 1                                                                                              
                                                                                                       
In [4]: print(obj.title)                                                                               
Project 1 

In [5]: print(obj.created)                                                                             
2021-10-17 12:39:56.327543+00:00 
                                                                                        
In [6]: print(project.review_set.all())                                                               
<QuerySet [<Review: up>]>                                                                              


mysql> SELECT
    -> projects_project.title,
    -> projects_review.value
    -> FROM projects_review
    -> INNER JOIN projects_project ON projects_review.project_id=projects_project.id
    -> WHERE projects_project.title="Project 1";
+-----------+-------+
| title     | value |
+-----------+-------+
| Project 1 | up    |
+-----------+-------+
1 row in set (0.00 sec)


mysql> SELECT
    -> projects_project.title,
    -> projects_review.value
    -> FROM projects_review
    -> INNER JOIN projects_project ON projects_review.project_id=projects_project.id
    -> WHERE projects_project.title="Project 5" OR projects_review.value="up";
+-----------+-------+
| title     | value |
+-----------+-------+
| Project 5 | up    |
| Project 1 | up    |
| Project 3 | up    |
+-----------+-------+
3 rows in set (0.00 sec)


SELECT
projects_project.title,
projects_review.value
FROM projects_review
INNER JOIN projects_project ON projects_review.project_id=projects_project.id
WHERE projects_project.title="Project 5" OR projects_review.value="up";
+-----------+
| title     |
+-----------+
| Project 5 |
| Project 1 |
| Project 3 |
+-----------+
3 rows in set (0.00 sec)


### INNER JOIN - projects_project table and projects_tag table
###            - ManyToMany relationship

### DJANGO QUERYSET
                  
In [1]: from projects.models import Project                                                            
                                                                                             
In [2]: obj = Project.objects.get(title="Project 1")                                                   
                                                                                                       
In [3]: print(obj)                                                                                     
Project 1                                                                                              
                                                                                                       
In [4]: print(obj.title)                                                                               
Project 1 

In [5]: print(obj.created)                                                                             
2021-10-17 12:39:56.327543+00:00 
                                                                                        
In [6]: print(project.review_set.all())                                                               
<QuerySet [<Review: up>]>  
                                                                      
In [7]: print(project.tags.all())                                                                     
<QuerySet [<Tag: Tag 10>, <Tag: Tag 6>]> 


### SQL

### There are 3 tables:

mysql> select * from projects_tag;
+--------+----------------------------+----------------------------------+
| name   | created                    | id                               |
+--------+----------------------------+----------------------------------+
| Tag 1  | 2021-10-17 12:33:49.880686 | 03bbd8ece7cc4b7b8860a6cc65b76826 |
| Tag 3  | 2021-10-17 12:33:58.181618 | 041b202c3cee44e181e419a77955b2db |
| Tag 9  | 2021-10-17 12:34:25.849937 | 13f70470d74f4ccfafeeff42d0d39f13 |
| Tag 4  | 2021-10-17 12:34:02.128582 | 5218cfb3c17d4108bc1c968029a0e0e9 |
| Tag 2  | 2021-10-17 12:33:54.133312 | bac2122274fe4dc79884b5cc63461cf9 |
| Tag 5  | 2021-10-17 12:34:06.561916 | c94dd573f7304763848c43a6884145ad |
| Tag 8  | 2021-10-17 12:34:22.111321 | d6d85179cdcd4bdca8e65427d03917fb |
| Tag 7  | 2021-10-17 12:34:18.046072 | ec377d68e4c947c7a2929c92d9dbfa0e |
| Tag 10 | 2021-10-17 12:34:30.553520 | ee313b7418a5498c9addbcefb80f1121 |
| Tag 6  | 2021-10-17 12:34:13.034582 | efaf38a113c04b11bad33a60b111ceaa |
+--------+----------------------------+----------------------------------+
10 rows in set (0.00 sec)

mysql> select * from projects_project_tags;
+----+----------------------------------+----------------------------------+
| id | project_id                       | tag_id                           |
+----+----------------------------------+----------------------------------+
|  1 | 13d7d7329a6d4b3eb1bf40c51f1cac86 | 03bbd8ece7cc4b7b8860a6cc65b76826 |
|  2 | 13d7d7329a6d4b3eb1bf40c51f1cac86 | 13f70470d74f4ccfafeeff42d0d39f13 |
|  5 | 488bbab1457b4e3887bce54e3d01a3c8 | 5218cfb3c17d4108bc1c968029a0e0e9 |
|  6 | 488bbab1457b4e3887bce54e3d01a3c8 | bac2122274fe4dc79884b5cc63461cf9 |
|  7 | 979fb56014ae497b908246d6ee5f3939 | ee313b7418a5498c9addbcefb80f1121 |
|  8 | 979fb56014ae497b908246d6ee5f3939 | efaf38a113c04b11bad33a60b111ceaa |
| 11 | d9d1a7b2caf5459aabb884b0e52c40c0 | 13f70470d74f4ccfafeeff42d0d39f13 |
| 10 | d9d1a7b2caf5459aabb884b0e52c40c0 | bac2122274fe4dc79884b5cc63461cf9 |
|  9 | d9d1a7b2caf5459aabb884b0e52c40c0 | c94dd573f7304763848c43a6884145ad |
|  3 | e490873bb23b4182a6d69cacf765d534 | 041b202c3cee44e181e419a77955b2db |
|  4 | e490873bb23b4182a6d69cacf765d534 | 5218cfb3c17d4108bc1c968029a0e0e9 |
+----+----------------------------------+----------------------------------+
11 rows in set (0.00 sec)

mysql> select title, description, id, vote_total, vote_ratio from projects_project;
+-----------+-----------------------+----------------------------------+------------+------------+
| title     | description           | id                               | vote_total | vote_ratio |
+-----------+-----------------------+----------------------------------+------------+------------+
| Project 1 | Project 1 description | 13d7d7329a6d4b3eb1bf40c51f1cac86 |        123 |         67 |
| Project 3 | Project 3 description | 488bbab1457b4e3887bce54e3d01a3c8 |         24 |         68 |
| Project 4 | Project 4 description | 979fb56014ae497b908246d6ee5f3939 |        120 |         88 |
| Project 5 | Project 5 description | d9d1a7b2caf5459aabb884b0e52c40c0 |        234 |         89 |
| Project 2 | Project 2 description | e490873bb23b4182a6d69cacf765d534 |         34 |         50 |
+-----------+-----------------------+----------------------------------+------------+------------+
5 rows in set (0.00 sec)

1.projects_tag
2.projects_project_tags
3.projects_project

project     project_tag       tag
Users       UserAddresses     Addresses
=======     =============     =========
Id          Id                Id
FirstName   UserId            City
LastName    AddressId         State
                              Zip
======================================

Users =  projects_project 
Id=id   
UserAddresses =  projects_project_tags  
Id=id, project_id, tag_id
Addresses=projects_tag
Id=id



mysql> SELECT projects_project.*                                                   
    -> FROM  projects_tag                                                          
    -> INNER JOIN                                                                  
    -> projects_project_tags ON projects_tag.id = projects_project_tags.tag_id     
    -> INNER JOIN                                                                  
    -> projects_project ON projects_project_tags.project_id = projects_project.id  
    -> WHERE (projects_tag.id = @tag_id);                                          
Empty set (0.00 sec)                                                               
                                                                                   
mysql> SELECT projects_tag.*                                                       
    -> FROM projects_tag                                                           
    -> INNER JOIN                                                                  
    -> projects_project_tags ON projects_tag.id = projects_project_tags.tag_id     
    -> INNER JOIN                                                                  
    -> projects_project ON projects_project_tags.project_id = projects_project.id  
    -> WHERE (projects_project.id = @project_id);                                  
Empty set (0.00 sec)  

# ///////////////////////// end ori ////////////////////////

# ///////////////////////// new ////////////////////////////

mysql> SHOW TABLES;
+--------------------------------+
| Tables_in_2024_dj5_kamubisaapa |
+--------------------------------+
| auth_group                     |
| auth_group_permissions         |
| auth_permission                |
| auth_user                      |
| auth_user_groups               |
| auth_user_user_permissions     |
| django_admin_log               |
| django_content_type            |
| django_migrations              |
| django_session                 |
| projects_project               |
| projects_project_tags          |
| projects_review                |
| projects_tag                   |
+--------------------------------+
14 rows in set (0.00 sec)

mysql> DESC projects_project;
+----------------+---------------+------+-----+---------+-------+
| Field          | Type          | Null | Key | Default | Extra |
+----------------+---------------+------+-----+---------+-------+
| title          | varchar(200)  | NO   |     | NULL    |       |
| description    | longtext      | YES  |     | NULL    |       |
| demo_link      | varchar(2000) | YES  |     | NULL    |       |
| source_link    | varchar(2000) | YES  |     | NULL    |       |
| created        | datetime(6)   | NO   |     | NULL    |       |
| id             | char(32)      | NO   | PRI | NULL    |       |
| featured_image | varchar(100)  | YES  |     | NULL    |       |
| vote_ratio     | int           | YES  |     | NULL    |       |
| vote_total     | int           | YES  |     | NULL    |       |
+----------------+---------------+------+-----+---------+-------+
9 rows in set (0.00 sec)

mysql> DESC projects_project_tags;
+------------+----------+------+-----+---------+----------------+
| Field      | Type     | Null | Key | Default | Extra          |
+------------+----------+------+-----+---------+----------------+
| id         | bigint   | NO   | PRI | NULL    | auto_increment |
| project_id | char(32) | NO   | MUL | NULL    |                |
| tag_id     | char(32) | NO   | MUL | NULL    |                |
+------------+----------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> DESC projects_review;
+------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| body       | longtext     | YES  |     | NULL    |       |
| value      | varchar(200) | NO   |     | NULL    |       |
| created    | datetime(6)  | NO   |     | NULL    |       |
| id         | char(32)     | NO   | PRI | NULL    |       |
| project_id | char(32)     | NO   | MUL | NULL    |       |
+------------+--------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

mysql> DESC projects_tag;
+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| name    | varchar(200) | NO   |     | NULL    |       |
| created | datetime(6)  | NO   |     | NULL    |       |
| id      | char(32)     | NO   | PRI | NULL    |       |
+---------+--------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM  projects_project;
+-----------+-----------------------+-----------------------+-----------------------+----------------------------+----------------------------------+----------------+------------+------------+
| title     | description           | demo_link             | source_link           | created                    | id                               | featured_image | vote_ratio | vote_total |
+-----------+-----------------------+-----------------------+-----------------------+----------------------------+----------------------------------+----------------+------------+------------+
| Project 3 | Project 3 description | https://www.demo3.com | https://www.demo3.com | 2024-02-27 09:44:19.568896 | 181697c7cb8644399026e3afad514644 | color1.PNG     |          0 |          0 |
| Project 2 | Project 2 description | https://www.demo2.com | https://www.demo2.com | 2024-02-27 07:49:55.074515 | 3b3be2857cb54a7ab9001c96424c6d17 | default.jpg    |          0 |          0 |
| Project 1 | Project 1 description | https://www.demo1.com | https://www.demo1.com | 2024-02-27 07:49:30.719706 | 57fe3df7aa954891aca2717d2ce3d4ed | default.jpg    |          0 |          0 |
+-----------+-----------------------+-----------------------+-----------------------+----------------------------+----------------------------------+----------------+------------+------------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM projects_project_tags;
+----+----------------------------------+----------------------------------+
| id | project_id                       | tag_id                           |
+----+----------------------------------+----------------------------------+
|  3 | 3b3be2857cb54a7ab9001c96424c6d17 | 034ef9817e374ed6a78483fcae46549a |
|  1 | 57fe3df7aa954891aca2717d2ce3d4ed | 034ef9817e374ed6a78483fcae46549a |
|  2 | 57fe3df7aa954891aca2717d2ce3d4ed | 179fb749faaf45c1a0d10fbf778ef257 |
+----+----------------------------------+----------------------------------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM  projects_review;
+------------+-------+----------------------------+----------------------------------+----------------------------------+
| body       | value | created                    | id                               | project_id                       |
+------------+-------+----------------------------+----------------------------------+----------------------------------+
| Good job.  | up    | 2024-02-27 10:16:32.887908 | 0a899336288145f08ffe1c7d8031477c | 181697c7cb8644399026e3afad514644 |
| Well done! | up    | 2024-02-27 13:57:50.040587 | 3a8c261640d84ef180a12d4f00a04f61 | 3b3be2857cb54a7ab9001c96424c6d17 |
+------------+-------+----------------------------+----------------------------------+----------------------------------+
2 rows in set (0.00 sec)

mysql> SELECT * FROM projects_tag;
+-------+----------------------------+----------------------------------+
| name  | created                    | id                               |
+-------+----------------------------+----------------------------------+
| Tag 2 | 2024-02-27 13:04:14.064684 | 034ef9817e374ed6a78483fcae46549a |
| Tag 1 | 2024-02-27 13:04:08.099079 | 179fb749faaf45c1a0d10fbf778ef257 |
+-------+----------------------------+----------------------------------+
2 rows in set (0.00 sec)


(bisaapa) λ python manage.py shell
...
>>>

>>> from app.projects.models import Project
>>> projects = Project.objects.all()
>>> print(projects)
<QuerySet [
	<Project: Project 3>, 
	<Project: Project 2>, 
	<Project: Project 1>]>

>>> print(projects.query)
SELECT 
	`projects_project`.`title`, 
	`projects_project`.`description`, 
	`projects_project`.`featured_image`, 
	`projects_project`.`demo_link`, 
	`projects_project`.`source_link`, 
	`projects_project`.`vote_total`, 
	`projects_project`.`vote_ratio`, 
	`projects_project`.`created`, 
	`projects_project`.`id` 
FROM `projects_project`


>>> obj = Project.objects.filter(title="Project 1")
>>> print(obj)
<QuerySet [<Project: Project 1>]>

>>> print(obj.query)
SELECT 
	`projects_project`.`title`, 
	`projects_project`.`description`, 
	`projects_project`.`featured_image`, 
	`projects_project`.`demo_link`, 
	`projects_project`.`source_link`, 
	`projects_project`.`vote_total`, 
	`projects_project`.`vote_ratio`, 
	`projects_project`.`created`, 
	`projects_project`.`id` 
FROM `projects_project` 
WHERE `projects_project`.`title` = Project 1


mysql> SELECT title FROM projects_project;
+-----------+
| title     |
+-----------+
| Project 3 |
| Project 2 |
| Project 1 |
+-----------+
3 rows in set (0.00 sec)

