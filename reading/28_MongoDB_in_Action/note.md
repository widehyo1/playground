tutorial> db.users.insert({username: "smith"})
DeprecationWarning: Collection.insert() is deprecated. Use insertOne, insertMany, or bulkWrite.
{
  acknowledged: true,
  insertedIds: { '0': ObjectId('68ecfbea38c32a7557ce5f47') }
}

tutorial> db.users.count()
DeprecationWarning: Collection.count() is deprecated. Use countDocuments or estimatedDocumentCount.
2

tutorial> db.users.find()
[
  { _id: ObjectId('68ecfbea38c32a7557ce5f47'), username: 'smith' },
  { _id: ObjectId('68ecfc2738c32a7557ce5f48'), username: 'jones' }
]
tutorial> db.users.find({username: "jones"})
[ { _id: ObjectId('68ecfc2738c32a7557ce5f48'), username: 'jones' } ]
tutorial> db.users.find({username: "jones", _id: "68ecfc2738c32a7557ce5f48"})

tutorial> db.users.find({username: "jones", _id: ObjectId("68ecfc2738c32a7557ce5f48")})
[ { _id: ObjectId('68ecfc2738c32a7557ce5f48'), username: 'jones' } ]
tutorial> db.users.find({ $and: [ { _id: ObjectId("68ecfc2738c32a7557ce5f48") }, { username: "jones" } ] })
[ { _id: ObjectId('68ecfc2738c32a7557ce5f48'), username: 'jones' } ]
tutorial> db.users.find({ $or: [ {username: "jones"}, {username: "smith"} ] })
[
  { _id: ObjectId('68ecfbea38c32a7557ce5f47'), username: 'smith' },
  { _id: ObjectId('68ecfc2738c32a7557ce5f48'), username: 'jones' }
]
tutorial> db.users.update({username: "smith"}, {$set: {country: "Canada"}})
DeprecationWarning: Collection.update() is deprecated. Use updateOne, updateMany, or bulkWrite.
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}

db.users.updateOne({username: "smith"}, {$set: {
  favorites: {
    cities: ["Chicago", "Cheyenne"],
    movies: ["Casablanca", "For a Few Dollars More", "The Sting"]
  }
}})

db.users.updateOne({username: "jones"}, {$set: {
  favorites: {
    movies: ["Casablanca", "Rocky"]
  }
}})

db.users.updateMany({"favorites.movies": "Casablanca"},
  {$addToSet: { "favorites.movies": "The Maltese Falcon"}},
  false,
  true
)

tutorial> load("work.js")
true
tutorial> db.users.find().pretty()
[
  {
    _id: ObjectId('68ecfbea38c32a7557ce5f47'),
    username: 'smith',
    favorites: {
      cities: [ 'Chicago', 'Cheyenne' ],
      movies: [
        'Casablanca',
        'For a Few Dollars More',
        'The Sting',
        'The Maltese Falcon'
      ]
    }
  },
  {
    _id: ObjectId('68ecfc2738c32a7557ce5f48'),
    username: 'jones',
    favorites: { movies: [ 'Casablanca', 'Rocky', 'The Maltese Falcon' ] }
  }
]
tutorial> db.users.remove({"favorites.cities": "Cheyenne"})
DeprecationWarning: Collection.remove() is deprecated. Use deleteOne, deleteMany, findOneAndDelete, or bulkWrite.
{ acknowledged: true, deletedCount: 1 }
tutorial> db.users.drop()
true

tutorial> db.users.remove({"favorites.cities": "Cheyenne"})
DeprecationWarning: Collection.remove() is deprecated. Use deleteOne, deleteMany, findOneAndDelete, or bulkWrite.
{ acknowledged: true, deletedCount: 1 }


tutorial> db.numbers.find( {num: {"$gt": 19995}}).explain("executionStats")
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'tutorial.numbers',
    indexFilterSet: false,
    parsedQuery: { num: { '$gt': 19995 } },
    queryHash: '483028BB',
    planCacheKey: '483028BB',
    optimizationTimeMillis: 0,
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    winningPlan: {
      stage: 'COLLSCAN',
      filter: { num: { '$gt': 19995 } },
      direction: 'forward'
    },
    rejectedPlans: []
  },
  executionStats: {
    executionSuccess: true,
    nReturned: 4,
    executionTimeMillis: 8,
    totalKeysExamined: 0,
    totalDocsExamined: 20000,
    executionStages: {
      stage: 'COLLSCAN',
      filter: { num: { '$gt': 19995 } },
      nReturned: 4,
      executionTimeMillisEstimate: 0,
      works: 20001,
      advanced: 4,
      needTime: 19996,
      needYield: 0,
      saveState: 20,
      restoreState: 20,
      isEOF: 1,
      direction: 'forward',
      docsExamined: 20000
    }
  },
  command: {
    find: 'numbers',
    filter: { num: { '$gt': 19995 } },
    '$db': 'tutorial'
  },
  serverInfo: {
    host: 'Win11-01',
    port: 27017,
    version: '7.0.25',
    gitVersion: '96dce3da49b8d2e9e0d328048cb56930eb1bdb2b'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600,
    internalQueryFrameworkControl: 'forceClassicEngine'
  },
  ok: 1
}
tutorial> db.numbers.createIndex({num: 1})
num_1
tutorial> db.numbers.getIndexes()
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { num: 1 }, name: 'num_1' }
]
tutorial> db.numbers.find( {num: {"$gt": 19995}}).explain("executionStats")
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'tutorial.numbers',
    indexFilterSet: false,
    parsedQuery: { num: { '$gt': 19995 } },
    queryHash: '483028BB',
    planCacheKey: '3FAA787B',
    optimizationTimeMillis: 0,
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    winningPlan: {
      stage: 'FETCH',
      inputStage: {
        stage: 'IXSCAN',
        keyPattern: { num: 1 },
        indexName: 'num_1',
        isMultiKey: false,
        multiKeyPaths: { num: [] },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: { num: [ '(19995, inf.0]' ] }
      }
    },
    rejectedPlans: []
  },
  executionStats: {
    executionSuccess: true,
    nReturned: 4,
    executionTimeMillis: 1,
    totalKeysExamined: 4,
    totalDocsExamined: 4,
    executionStages: {
      stage: 'FETCH',
      nReturned: 4,
      executionTimeMillisEstimate: 0,
      works: 5,
      advanced: 4,
      needTime: 0,
      needYield: 0,
      saveState: 0,
      restoreState: 0,
      isEOF: 1,
      docsExamined: 4,
      alreadyHasObj: 0,
      inputStage: {
        stage: 'IXSCAN',
        nReturned: 4,
        executionTimeMillisEstimate: 0,
        works: 5,
        advanced: 4,
        needTime: 0,
        needYield: 0,
        saveState: 0,
        restoreState: 0,
        isEOF: 1,
        keyPattern: { num: 1 },
        indexName: 'num_1',
        isMultiKey: false,
        multiKeyPaths: { num: [] },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: { num: [ '(19995, inf.0]' ] },
        keysExamined: 4,
        seeks: 1,
        dupsTested: 0,
        dupsDropped: 0
      }
    }
  },
  command: {
    find: 'numbers',
    filter: { num: { '$gt': 19995 } },
    '$db': 'tutorial'
  },
  serverInfo: {
    host: 'Win11-01',
    port: 27017,
    version: '7.0.25',
    gitVersion: '96dce3da49b8d2e9e0d328048cb56930eb1bdb2b'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600,
    internalQueryFrameworkControl: 'forceClassicEngine'
  },
  ok: 1
}
tutorial> 

db.products.createIndex({slug: 1}, {unique: true})

db.products.insertOne({name: "Extra Large Wheelbarrow", sku: "9092", slug: "wheelbarrow-9092"})

db.categories.insertOne(newCategory)

newUser = {
    username: "kbanker",
    email: "kbanker@gmail.com",
    first_name: "Kyle",
    last_name: "Banker",
    hashed_password: "asdf",
    addresses: [
        {
            name: "work",
            street: "1 E. 23rd Street",
            city: "New York",
            state: "NY",
            zip: 10010
        }
    ]
};



---

2025.10.22
