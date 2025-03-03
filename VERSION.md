Original Version - VScode MongoDB Extension

MongoDB Website:

To run MongoDB (i.e. the mongod process) as a macOS service, run:
brew services start mongodb-community@8.0

To stop a mongod running as a macOS service, use the following command as needed:
brew services stop mongodb-community@8.0


Installed Extension:
- Collection is a group of documents
- Database is a group of collections
To start MongoDB shell(Mongosh):
mongosh

To stop running MongoDB shell:
exit

Notes(Alternatively, use MongoDB compass)

cls - clear screen

show dbs - show current databases

use <DB_NAME> - Access a database

db.createCollection() - Create a collection within database

db.dropDatabase() - Drop a database

Insert:
db.<Collection_Name>.insertOne({field1: val1, field2: val2, field3: val3})
db.<Collection_Name>.insertMany({field1: val1, field2: val2, field3: val3},{field1: val1, field2: val2, field3: val3},{field1: val1, field2: val2, field3: val3})

find:
*Each document is enclosed within a set of curly braces
*Within each document, you can have as many field value pairs as you like. They all don't need to be consistent.
db.<Collection_Name>.find() - shows current objects in collection

db.<Collection_Name>.find({query},{projection}) 
db.<Collection_Name>.find({query1,query2,...},{field1: true/false,...}) 
**First paramater is where clause in SQL
**Empty first paramater indicates all documents in collection

DataTypes:
Int
Double
String
Date - new Date()
null
Array - []
Nested Documents: {field1: val1, ...}

Sorting and Limiting: 
db.students.find().sort({field: 1(alphabetical order), -1(reverse alphabetical order)})

db.students.find().sort({field: 1(ascending order), -1(descending order)})

db.students.find().limit(<Number>) - limit the documents returned by objectID

*sort and limit can be merged to form queries

Update:

db.<Collection_Name>.updateOne(filter, update)
filter = seleciton criteria
update = update paramater
    $set:{} - update or insert a field
    $unset:{} - remove a field(set field to an empty string)

db.<Collection_Name>.updateMany(filter, update)

$exists to check if a field is empty or not

Deletion:

db.students.deleteOne({filter})
db.students.deleteMany({filter})

{fieldName:{$exists:false}}

Logical Operators:

$ne = not equal to
$lt = less than
$lte = less than equal to
$gt = greater than
$gte = greater than equal to

To find documents within a range: $gte: value, $lte: value

$in:[] = document values are in the following array
$nin:[] = documents do not have any of the values in the array

$and:[{condition1}, {condition2}]

$or:[{condition1}, {condition2}]

$nor:[{condition1}, {condition2}] = both conditions need to be false

$not:{}

Indexes:
-Speeding Up Query Execution
- Without indexes, MongoDB performs a collection scan, examining every document to find matching query results. This is slow for large datasets.
- Indexes allow MongoDB to quickly narrow down the search to relevant documents, improving performance.

db.students.createIndex({fieldName: 1(ascending) -1(descending)}) = Allows for quicker lookups in fields

db.students.getIndexes() = Display all indexes

db.students.dropIndex(<IndexName>)

Collections:

show collections - shows all collections in current DB

db.createCollection("teachers", {capped: true, size:<Bytes>, max: <#_Documents>}, {autoIndexID:true/false})

db.<Collection_Name>.drop()
