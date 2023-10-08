/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "t385mkxgmzit0hg",
    "created": "2023-10-08 08:56:46.458Z",
    "updated": "2023-10-08 08:56:46.458Z",
    "name": "test_collection2",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "6ocnmfaw",
        "name": "money",
        "type": "number",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "noDecimal": false
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("t385mkxgmzit0hg");

  return dao.deleteCollection(collection);
})
