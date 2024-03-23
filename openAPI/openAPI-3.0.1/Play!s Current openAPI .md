

```
{
  "openapi": "3.0.1",
  "info": {
    "title": "standard public schema",
    "description": "",
    "version": "12.0.2"
  },
  "externalDocs": {
    "description": "PostgREST Documentation",
    "url": "https://postgrest.org/en/v12.0/api.html"
  },
  "servers": [
    {
      "url": "https://api-1.fountain.coach"
    }
  ],
  "paths": {
    "/": {
      "get": {
        "tags": [
          "Introspection"
        ],
        "summary": "OpenAPI description (this document)",
        "responses": {
          "200": {
            "description": "OK",
            "content": {}
          }
        },
        "operationId": "getRoot"
      }
    },
    "/plays": {
      "get": {
        "tags": [
          "plays"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "integer"
            }
          },
          {
            "name": "title",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "character varying"
            }
          },
          {
            "name": "author",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "character varying"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "title"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "title": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      },
                      "author": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying",
                        "default": "William Shakespeare"
                      }
                    }
                  }
                }
              },
              "application/vnd.pgrst.object+json;nulls=stripped": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "title"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "title": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      },
                      "author": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying",
                        "default": "William Shakespeare"
                      }
                    }
                  }
                }
              },
              "application/vnd.pgrst.object+json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "title"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "title": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      },
                      "author": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying",
                        "default": "William Shakespeare"
                      }
                    }
                  }
                }
              },
              "text/csv": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "title"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "title": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      },
                      "author": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying",
                        "default": "William Shakespeare"
                      }
                    }
                  }
                }
              }
            }
          },
          "206": {
            "description": "Partial Content",
            "content": {}
          }
        },
        "operationId": "getPlays"
      },
      "post": {
        "tags": [
          "plays"
        ],
        "parameters": [
          {
            "name": "select",
            "in": "query",
            "description": "Filtering Columns",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "plays",
          "content": {
            "application/json": {
              "schema": {
                "required": [
                  "id",
                  "title"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "author": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying",
                    "default": "William Shakespeare"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json;nulls=stripped": {
              "schema": {
                "required": [
                  "id",
                  "title"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "author": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying",
                    "default": "William Shakespeare"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json": {
              "schema": {
                "required": [
                  "id",
                  "title"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "author": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying",
                    "default": "William Shakespeare"
                  }
                }
              }
            },
            "text/csv": {
              "schema": {
                "required": [
                  "id",
                  "title"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "author": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying",
                    "default": "William Shakespeare"
                  }
                }
              }
            }
          },
          "required": false
        },
        "responses": {
          "201": {
            "description": "Created",
            "content": {}
          }
        },
        "x-codegen-request-body-name": "plays",
        "operationId": "postPlays"
      },
      "patch": {
        "tags": [
          "plays"
        ],
        "parameters": [],
        "requestBody": {
          "description": "plays",
          "content": {
            "application/json": {
              "schema": {
                "required": [
                  "id",
                  "title"
                ],
                "type": "object",
                "properties": {
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "author": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying",
                    "default": "William Shakespeare"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json;nulls=stripped": {
              "schema": {
                "required": [
                  "id",
                  "title"
                ],
                "type": "object",
                "properties": {
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "author": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying",
                    "default": "William Shakespeare"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json": {
              "schema": {
                "required": [
                  "id",
                  "title"
                ],
                "type": "object",
                "properties": {
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "author": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying",
                    "default": "William Shakespeare"
                  }
                }
              }
            },
            "text/csv": {
              "schema": {
                "required": [
                  "id",
                  "title"
                ],
                "type": "object",
                "properties": {
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "author": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying",
                    "default": "William Shakespeare"
                  }
                }
              }
            }
          },
          "required": false
        },
        "responses": {
          "204": {
            "description": "No Content",
            "content": {}
          }
        },
        "x-codegen-request-body-name": "plays",
        "operationId": "patchPlays"
      }
    },
    "/acts": {
      "get": {
        "tags": [
          "acts"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "integer"
            }
          },
          {
            "name": "play_id",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "integer"
            }
          },
          {
            "name": "number",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "integer"
            }
          },
          {
            "name": "title",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "character varying"
            }
          },
          {
            "name": "select",
            "in": "query",
            "description": "Filtering Columns",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "order",
            "in": "query",
            "description": "Ordering",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Limiting and Pagination",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Limiting and Pagination",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "number"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "play_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                        "format": "integer"
                      },
                      "number": {
                        "type": "integer",
                        "format": "integer"
                      },
                      "title": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      }
                    }
                  }
                }
              },
              "application/vnd.pgrst.object+json;nulls=stripped": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "number"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "play_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                        "format": "integer"
                      },
                      "number": {
                        "type": "integer",
                        "format": "integer"
                      },
                      "title": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      }
                    }
                  }
                }
              },
              "application/vnd.pgrst.object+json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "number"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "play_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                        "format": "integer"
                      },
                      "number": {
                        "type": "integer",
                        "format": "integer"
                      },
                      "title": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      }
                    }
                  }
                }
              },
              "text/csv": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "number"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "play_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                        "format": "integer"
                      },
                      "number": {
                        "type": "integer",
                        "format": "integer"
                      },
                      "title": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      }
                    }
                  }
                }
              }
            }
          },
          "206": {
            "description": "Partial Content",
            "content": {}
          }
        },
        "operationId": "getActs"
      },
      "post": {
        "tags": [
          "acts"
        ],
        "parameters": [
          {
            "name": "select",
            "in": "query",
            "description": "Filtering Columns",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "acts",
          "content": {
            "application/json": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "play_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                    "format": "integer"
                  },
                  "number": {
                    "type": "integer",
                    "format": "integer"
                  },
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json;nulls=stripped": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "play_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                    "format": "integer"
                  },
                  "number": {
                    "type": "integer",
                    "format": "integer"
                  },
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "play_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                    "format": "integer"
                  },
                  "number": {
                    "type": "integer",
                    "format": "integer"
                  },
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            },
            "text/csv": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "play_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                    "format": "integer"
                  },
                  "number": {
                    "type": "integer",
                    "format": "integer"
                  },
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            }
          },
          "required": false
        },
        "responses": {
          "201": {
            "description": "Created",
            "content": {}
          }
        },
        "x-codegen-request-body-name": "acts",
        "operationId": "postActs"
      },
      "patch": {
        "tags": [
          "acts"
        ],
        "parameters": [],
        "requestBody": {
          "description": "acts",
          "content": {
            "application/json": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json;nulls=stripped": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            },
            "text/csv": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            }
          },
          "required": false
        },
        "responses": {
          "204": {
            "description": "No Content",
            "content": {}
          }
        },
        "x-codegen-request-body-name": "acts",
        "operationId": "patchActs"
      }
    },
    "/scenes": {
      "get": {
        "tags": [
          "scenes"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "integer"
            }
          },
          {
            "name": "act_id",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "integer"
            }
          },
          {
            "name": "number",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "integer"
            }
          },
          {
            "name": "title",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "character varying"
            }
          },
          {
            "name": "location",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "character varying"
            }
          },
          {
            "name": "select",
            "in": "query",
            "description": "Filtering Columns",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "order",
            "in": "query",
            "description": "Ordering",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Limiting and Pagination",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Limiting and Pagination",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "number"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "act_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `acts.id`.<fk table='acts' column='id'/>",
                        "format": "integer"
                      },
                      "number": {
                        "type": "integer",
                        "format": "integer"
                      },
                      "title": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      },
                      "location": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      }
                    }
                  }
                }
              },
              "application/vnd.pgrst.object+json;nulls=stripped": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "number"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "act_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `acts.id`.<fk table='acts' column='id'/>",
                        "format": "integer"
                      },
                      "number": {
                        "type": "integer",
                        "format": "integer"
                      },
                      "title": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      },
                      "location": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      }
                    }
                  }
                }
              },
              "application/vnd.pgrst.object+json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "number"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "act_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `acts.id`.<fk table='acts' column='id'/>",
                        "format": "integer"
                      },
                      "number": {
                        "type": "integer",
                        "format": "integer"
                      },
                      "title": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      },
                      "location": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      }
                    }
                  }
                }
              },
              "text/csv": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "number"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "act_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `acts.id`.<fk table='acts' column='id'/>",
                        "format": "integer"
                      },
                      "number": {
                        "type": "integer",
                        "format": "integer"
                      },
                      "title": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      },
                      "location": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      }
                    }
                  }
                }
              }
            }
          },
          "206": {
            "description": "Partial Content",
            "content": {}
          }
        },
        "operationId": "getScenes"
      },
      "post": {
        "tags": [
          "scenes"
        ],
        "parameters": [
          {
            "name": "select",
            "in": "query",
            "description": "Filtering Columns",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "scenes",
          "content": {
            "application/json": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "act_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `acts.id`.<fk table='acts' column='id'/>",
                    "format": "integer"
                  },
                  "number": {
                    "type": "integer",
                    "format": "integer"
                  },
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "location": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json;nulls=stripped": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "act_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `acts.id`.<fk table='acts' column='id'/>",
                    "format": "integer"
                  },
                  "number": {
                    "type": "integer",
                    "format": "integer"
                  },
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "location": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "act_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `acts.id`.<fk table='acts' column='id'/>",
                    "format": "integer"
                  },
                  "number": {
                    "type": "integer",
                    "format": "integer"
                  },
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "location": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            },
            "text/csv": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "act_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `acts.id`.<fk table='acts' column='id'/>",
                    "format": "integer"
                  },
                  "number": {
                    "type": "integer",
                    "format": "integer"
                  },
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "location": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            }
          },
          "required": false
        },
        "responses": {
          "201": {
            "description": "Created",
            "content": {}
          }
        },
        "x-codegen-request-body-name": "scenes",
        "operationId": "postScenes"
      },
      "patch": {
        "tags": [
          "scenes"
        ],
        "parameters": [],
        "requestBody": {
          "description": "scenes",
          "content": {
            "application/json": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json;nulls=stripped": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            },
            "text/csv": {
              "schema": {
                "required": [
                  "id",
                  "number"
                ],
                "type": "object",
                "properties": {
                  "title": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  }
                }
              }
            }
          },
          "required": false
        },
        "responses": {
          "204": {
            "description": "No Content",
            "content": {}
          }
        },
        "x-codegen-request-body-name": "scenes",
        "operationId": "patchScenes"
      }
    },
    "/characters": {
      "get": {
        "tags": [
          "characters"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "integer"
            }
          },
          {
            "name": "play_id",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "integer"
            }
          },
          {
            "name": "name",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "character varying"
            }
          },
          {
            "name": "description",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "text"
            }
          },
          {
            "name": "select",
            "in": "query",
            "description": "Filtering Columns",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "order",
            "in": "query",
            "description": "Ordering",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Limiting and Pagination",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Limiting and Pagination",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "name"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "play_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                        "format": "integer"
                      },
                      "name": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      },
                      "description": {
                        "type": "string",
                        "format": "text"
                      }
                    }
                  }
                }
              },
              "application/vnd.pgrst.object+json;nulls=stripped": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "name"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "play_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                        "format": "integer"
                      },
                      "name": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      },
                      "description": {
                        "type": "string",
                        "format": "text"
                      }
                    }
                  }
                }
              },
              "application/vnd.pgrst.object+json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "name"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "play_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                        "format": "integer"
                      },
                      "name": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      },
                      "description": {
                        "type": "string",
                        "format": "text"
                      }
                    }
                  }
                }
              },
              "text/csv": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "name"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "play_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                        "format": "integer"
                      },
                      "name": {
                        "maxLength": 255,
                        "type": "string",
                        "format": "character varying"
                      },
                      "description": {
                        "type": "string",
                        "format": "text"
                      }
                    }
                  }
                }
              }
            }
          },
          "206": {
            "description": "Partial Content",
            "content": {}
          }
        },
        "operationId": "getCharacters"
      },
      "post": {
        "tags": [
          "characters"
        ],
        "parameters": [
          {
            "name": "select",
            "in": "query",
            "description": "Filtering Columns",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "characters",
          "content": {
            "application/json": {
              "schema": {
                "required": [
                  "id",
                  "name"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "play_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                    "format": "integer"
                  },
                  "name": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "description": {
                    "type": "string",
                    "format": "text"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json;nulls=stripped": {
              "schema": {
                "required": [
                  "id",
                  "name"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "play_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                    "format": "integer"
                  },
                  "name": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "description": {
                    "type": "string",
                    "format": "text"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json": {
              "schema": {
                "required": [
                  "id",
                  "name"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "play_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                    "format": "integer"
                  },
                  "name": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "description": {
                    "type": "string",
                    "format": "text"
                  }
                }
              }
            },
            "text/csv": {
              "schema": {
                "required": [
                  "id",
                  "name"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "play_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                    "format": "integer"
                  },
                  "name": {
                    "maxLength": 255,
                    "type": "string",
                    "format": "character varying"
                  },
                  "description": {
                    "type": "string",
                    "format": "text"
                  }
                }
              }
            }
          },
          "required": false
        },
        "responses": {
          "201": {
            "description": "Created",
            "content": {}
          }
        },
        "x-codegen-request-body-name": "characters",
        "operationId": "postCharacters"
      },
      "patch": {
        "tags": [
          "characters"
        ],
        "parameters": [],
        "requestBody": {
          "description": "characters",
          "content": {
            "application/json": {
              "schema": {
                "required": [
                  "id",
                  "name"
                ],
                "type": "object",
                "properties": {}
              }
            },
            "application/vnd.pgrst.object+json;nulls=stripped": {
              "schema": {
                "required": [
                  "id",
                  "name"
                ],
                "type": "object",
                "properties": {}
              }
            },
            "application/vnd.pgrst.object+json": {
              "schema": {
                "required": [
                  "id",
                  "name"
                ],
                "type": "object",
                "properties": {}
              }
            },
            "text/csv": {
              "schema": {
                "required": [
                  "id",
                  "name"
                ],
                "type": "object",
                "properties": {}
              }
            }
          },
          "required": false
        },
        "responses": {
          "204": {
            "description": "No Content",
            "content": {}
          }
        },
        "x-codegen-request-body-name": "characters",
        "operationId": "patchCharacters"
      }
    },
    "/dialogues": {
      "get": {
        "tags": [
          "dialogues"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "integer"
            }
          },
          {
            "name": "scene_id",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "integer"
            }
          },
          {
            "name": "character_id",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "integer"
            }
          },
          {
            "name": "original_text",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "text"
            }
          },
          {
            "name": "modern_text",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "text"
            }
          },
          {
            "name": "sequence",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "original_text",
                      "sequence"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "scene_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `scenes.id`.<fk table='scenes' column='id'/>",
                        "format": "integer"
                      },
                      "character_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `characters.id`.<fk table='characters' column='id'/>",
                        "format": "integer"
                      },
                      "original_text": {
                        "type": "string",
                        "format": "text"
                      },
                      "modern_text": {
                        "type": "string",
                        "format": "text"
                      },
                      "sequence": {
                        "type": "integer",
                        "format": "integer"
                      }
                    }
                  }
                }
              },
              "application/vnd.pgrst.object+json;nulls=stripped": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "original_text",
                      "sequence"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "scene_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `scenes.id`.<fk table='scenes' column='id'/>",
                        "format": "integer"
                      },
                      "character_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `characters.id`.<fk table='characters' column='id'/>",
                        "format": "integer"
                      },
                      "original_text": {
                        "type": "string",
                        "format": "text"
                      },
                      "modern_text": {
                        "type": "string",
                        "format": "text"
                      },
                      "sequence": {
                        "type": "integer",
                        "format": "integer"
                      }
                    }
                  }
                }
              },
              "application/vnd.pgrst.object+json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "original_text",
                      "sequence"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "scene_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `scenes.id`.<fk table='scenes' column='id'/>",
                        "format": "integer"
                      },
                      "character_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `characters.id`.<fk table='characters' column='id'/>",
                        "format": "integer"
                      },
                      "original_text": {
                        "type": "string",
                        "format": "text"
                      },
                      "modern_text": {
                        "type": "string",
                        "format": "text"
                      },
                      "sequence": {
                        "type": "integer",
                        "format": "integer"
                      }
                    }
                  }
                }
              },
              "text/csv": {
                "schema": {
                  "type": "array",
                  "items": {
                    "required": [
                      "id",
                      "original_text",
                      "sequence"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Primary Key.<pk/>",
                        "format": "integer"
                      },
                      "scene_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `scenes.id`.<fk table='scenes' column='id'/>",
                        "format": "integer"
                      },
                      "character_id": {
                        "type": "integer",
                        "description": "Note:\nThis is a Foreign Key to `characters.id`.<fk table='characters' column='id'/>",
                        "format": "integer"
                      },
                      "original_text": {
                        "type": "string",
                        "format": "text"
                      },
                      "modern_text": {
                        "type": "string",
                        "format": "text"
                      },
                      "sequence": {
                        "type": "integer",
                        "format": "integer"
                      }
                    }
                  }
                }
              }
            }
          },
          "206": {
            "description": "Partial Content",
            "content": {}
          }
        },
        "operationId": "getDialogues"
      },
      "post": {
        "tags": [
          "dialogues"
        ],
        "parameters": [
          {
            "name": "select",
            "in": "query",
            "description": "Filtering Columns",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "dialogues",
          "content": {
            "application/json": {
              "schema": {
                "required": [
                  "id",
                  "original_text",
                  "sequence"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "scene_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `scenes.id`.<fk table='scenes' column='id'/>",
                    "format": "integer"
                  },
                  "character_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `characters.id`.<fk table='characters' column='id'/>",
                    "format": "integer"
                  },
                  "original_text": {
                    "type": "string",
                    "format": "text"
                  },
                  "modern_text": {
                    "type": "string",
                    "format": "text"
                  },
                  "sequence": {
                    "type": "integer",
                    "format": "integer"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json;nulls=stripped": {
              "schema": {
                "required": [
                  "id",
                  "original_text",
                  "sequence"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "scene_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `scenes.id`.<fk table='scenes' column='id'/>",
                    "format": "integer"
                  },
                  "character_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `characters.id`.<fk table='characters' column='id'/>",
                    "format": "integer"
                  },
                  "original_text": {
                    "type": "string",
                    "format": "text"
                  },
                  "modern_text": {
                    "type": "string",
                    "format": "text"
                  },
                  "sequence": {
                    "type": "integer",
                    "format": "integer"
                  }
                }
              }
            },
            "application/vnd.pgrst.object+json": {
              "schema": {
                "required": [
                  "id",
                  "original_text",
                  "sequence"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "scene_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `scenes.id`.<fk table='scenes' column='id'/>",
                    "format": "integer"
                  },
                  "character_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `characters.id`.<fk table='characters' column='id'/>",
                    "format": "integer"
                  },
                  "original_text": {
                    "type": "string",
                    "format": "text"
                  },
                  "modern_text": {
                    "type": "string",
                    "format": "text"
                  },
                  "sequence": {
                    "type": "integer",
                    "format": "integer"
                  }
                }
              }
            },
            "text/csv": {
              "schema": {
                "required": [
                  "id",
                  "original_text",
                  "sequence"
                ],
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Primary Key.<pk/>",
                    "format": "integer"
                  },
                  "scene_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `scenes.id`.<fk table='scenes' column='id'/>",
                    "format": "integer"
                  },
                  "character_id": {
                    "type": "integer",
                    "description": "Note:\nThis is a Foreign Key to `characters.id`.<fk table='characters' column='id'/>",
                    "format": "integer"
                  },
                  "original_text": {
                    "type": "string",
                    "format": "text"
                  },
                  "modern_text": {
                    "type": "string",
                    "format": "text"
                  },
                  "sequence": {
                    "type": "integer",
                    "format": "integer"
                  }
                }
              }
            }
          },
          "required": false
        },
        "responses": {
          "201": {
            "description": "Created",
            "content": {}
          }
        },
        "x-codegen-request-body-name": "dialogues",
        "operationId": "postDialogues"
      },
      "patch": {
        "tags": [
          "dialogues"
        ],
        "parameters": [],
        "requestBody": {
          "description": "dialogues",
          "content": {
            "application/json": {
              "schema": {
                "required": [
                  "id",
                  "original_text",
                  "sequence"
                ],
                "type": "object",
                "properties": {}
              }
            },
            "application/vnd.pgrst.object+json;nulls=stripped": {
              "schema": {
                "required": [
                  "id",
                  "original_text",
                  "sequence"
                ],
                "type": "object",
                "properties": {}
              }
            },
            "application/vnd.pgrst.object+json": {
              "schema": {
                "required": [
                  "id",
                  "original_text",
                  "sequence"
                ],
                "type": "object",
                "properties": {}
              }
            },
            "text/csv": {
              "schema": {
                "required": [
                  "id",
                  "original_text",
                  "sequence"
                ],
                "type": "object",
                "properties": {}
              }
            }
          },
          "required": false
        },
        "responses": {
          "204": {
            "description": "No Content",
            "content": {}
          }
        },
        "x-codegen-request-body-name": "dialogues",
        "operationId": "patchDialogues"
      }
    }
  },
  "components": {
    "schemas": {
      "plays": {
        "required": [
          "id",
          "title"
        ],
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Note:\nThis is a Primary Key.<pk/>",
            "format": "integer"
          },
          "title": {
            "maxLength": 255,
            "type": "string",
            "format": "character varying"
          },
          "author": {
            "maxLength": 255,
            "type": "string",
            "format": "character varying",
            "default": "William Shakespeare"
          }
        }
      },
      "dialogues": {
        "required": [
          "id",
          "original_text",
          "sequence"
        ],
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Note:\nThis is a Primary Key.<pk/>",
            "format": "integer"
          },
          "scene_id": {
            "type": "integer",
            "description": "Note:\nThis is a Foreign Key to `scenes.id`.<fk table='scenes' column='id'/>",
            "format": "integer"
          },
          "character_id": {
            "type": "integer",
            "description": "Note:\nThis is a Foreign Key to `characters.id`.<fk table='characters' column='id'/>",
            "format": "integer"
          },
          "original_text": {
            "type": "string",
            "format": "text"
          },
          "modern_text": {
            "type": "string",
            "format": "text"
          },
          "sequence": {
            "type": "integer",
            "format": "integer"
          }
        }
      },
      "scenes": {
        "required": [
          "id",
          "number"
        ],
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Note:\nThis is a Primary Key.<pk/>",
            "format": "integer"
          },
          "act_id": {
            "type": "integer",
            "description": "Note:\nThis is a Foreign Key to `acts.id`.<fk table='acts' column='id'/>",
            "format": "integer"
          },
          "number": {
            "type": "integer",
            "format": "integer"
          },
          "title": {
            "maxLength": 255,
            "type": "string",
            "format": "character varying"
          },
          "location": {
            "maxLength": 255,
            "type": "string",
            "format": "character varying"
          }
        }
      },
      "acts": {
        "required": [
          "id",
          "number"
        ],
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Note:\nThis is a Primary Key.<pk/>",
            "format": "integer"
          },
          "play_id": {
            "type": "integer",
            "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
            "format": "integer"
          },
          "number": {
            "type": "integer",
            "format": "integer"
          },
          "title": {
            "maxLength": 255,
            "type": "string",
            "format": "character varying"
          }
        }
      },
      "characters": {
        "required": [
          "id",
          "name"
        ],
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Note:\nThis is a Primary Key.<pk/>",
            "format": "integer"
          },
          "play_id": {
            "type": "integer",
            "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
            "format": "integer"
          },
          "name": {
            "maxLength": 255,
            "type": "string",
            "format": "character varying"
          },
          "description": {
            "type": "string",
            "format": "text"
          }
        }
      }
    },
    "parameters": {
      "select": {
        "name": "select",
        "in": "query",
        "description": "Filtering Columns",
        "schema": {
          "type": "string"
        }
      },
      "on_conflict": {
        "name": "on_conflict",
        "in": "query",
        "description": "On Conflict",
        "schema": {
          "type": "string"
        }
      },
      "order": {
        "name": "order",
        "in": "query",
        "description": "Ordering",
        "schema": {
          "type": "string"
        }
      },
      "offset": {
        "name": "offset",
        "in": "query",
        "description": "Limiting and Pagination",
        "schema": {
          "type": "string"
        }
      },
      "limit": {
        "name": "limit",
        "in": "query",
        "description": "Limiting and Pagination",
        "schema": {
          "type": "string"
        }
      },
      "rowFilter.plays.id": {
        "name": "id",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "integer"
        }
      },
      "rowFilter.plays.title": {
        "name": "title",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "character varying"
        }
      },
      "rowFilter.plays.author": {
        "name": "author",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "character varying"
        }
      },
      "rowFilter.dialogues.id": {
        "name": "id",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "integer"
        }
      },
      "rowFilter.dialogues.scene_id": {
        "name": "scene_id",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "integer"
        }
      },
      "rowFilter.dialogues.character_id": {
        "name": "character_id",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "integer"
        }
      },
      "rowFilter.dialogues.original_text": {
        "name": "original_text",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "text"
        }
      },
      "rowFilter.dialogues.modern_text": {
        "name": "modern_text",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "text"
        }
      },
      "rowFilter.dialogues.sequence": {
        "name": "sequence",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "integer"
        }
      },
      "rowFilter.scenes.id": {
        "name": "id",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "integer"
        }
      },
      "rowFilter.scenes.act_id": {
        "name": "act_id",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "integer"
        }
      },
      "rowFilter.scenes.number": {
        "name": "number",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "integer"
        }
      },
      "rowFilter.scenes.title": {
        "name": "title",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "character varying"
        }
      },
      "rowFilter.scenes.location": {
        "name": "location",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "character varying"
        }
      },
      "rowFilter.acts.id": {
        "name": "id",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "integer"
        }
      },
      "rowFilter.acts.play_id": {
        "name": "play_id",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "integer"
        }
      },
      "rowFilter.acts.number": {
        "name": "number",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "integer"
        }
      },
      "rowFilter.acts.title": {
        "name": "title",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "character varying"
        }
      },
      "rowFilter.characters.id": {
        "name": "id",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "integer"
        }
      },
      "rowFilter.characters.play_id": {
        "name": "play_id",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "integer"
        }
      },
      "rowFilter.characters.name": {
        "name": "name",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "character varying"
        }
      },
      "rowFilter.characters.description": {
        "name": "description",
        "in": "query",
        "schema": {
          "type": "string",
          "format": "text"
        }
      }
    },
    "requestBodies": {
      "body.plays": {
        "description": "plays",
        "content": {
          "application/json": {
            "schema": {
              "required": [
                "id",
                "title"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "title": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                },
                "author": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying",
                  "default": "William Shakespeare"
                }
              }
            }
          },
          "application/vnd.pgrst.object+json;nulls=stripped": {
            "schema": {
              "required": [
                "id",
                "title"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "title": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                },
                "author": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying",
                  "default": "William Shakespeare"
                }
              }
            }
          },
          "application/vnd.pgrst.object+json": {
            "schema": {
              "required": [
                "id",
                "title"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "title": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                },
                "author": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying",
                  "default": "William Shakespeare"
                }
              }
            }
          },
          "text/csv": {
            "schema": {
              "required": [
                "id",
                "title"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "title": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                },
                "author": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying",
                  "default": "William Shakespeare"
                }
              }
            }
          }
        },
        "required": false
      },
      "body.dialogues": {
        "description": "dialogues",
        "content": {
          "application/json": {
            "schema": {
              "required": [
                "id",
                "original_text",
                "sequence"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "scene_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `scenes.id`.<fk table='scenes' column='id'/>",
                  "format": "integer"
                },
                "character_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `characters.id`.<fk table='characters' column='id'/>",
                  "format": "integer"
                },
                "original_text": {
                  "type": "string",
                  "format": "text"
                },
                "modern_text": {
                  "type": "string",
                  "format": "text"
                },
                "sequence": {
                  "type": "integer",
                  "format": "integer"
                }
              }
            }
          },
          "application/vnd.pgrst.object+json;nulls=stripped": {
            "schema": {
              "required": [
                "id",
                "original_text",
                "sequence"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "scene_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `scenes.id`.<fk table='scenes' column='id'/>",
                  "format": "integer"
                },
                "character_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `characters.id`.<fk table='characters' column='id'/>",
                  "format": "integer"
                },
                "original_text": {
                  "type": "string",
                  "format": "text"
                },
                "modern_text": {
                  "type": "string",
                  "format": "text"
                },
                "sequence": {
                  "type": "integer",
                  "format": "integer"
                }
              }
            }
          },
          "application/vnd.pgrst.object+json": {
            "schema": {
              "required": [
                "id",
                "original_text",
                "sequence"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "scene_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `scenes.id`.<fk table='scenes' column='id'/>",
                  "format": "integer"
                },
                "character_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `characters.id`.<fk table='characters' column='id'/>",
                  "format": "integer"
                },
                "original_text": {
                  "type": "string",
                  "format": "text"
                },
                "modern_text": {
                  "type": "string",
                  "format": "text"
                },
                "sequence": {
                  "type": "integer",
                  "format": "integer"
                }
              }
            }
          },
          "text/csv": {
            "schema": {
              "required": [
                "id",
                "original_text",
                "sequence"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "scene_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `scenes.id`.<fk table='scenes' column='id'/>",
                  "format": "integer"
                },
                "character_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `characters.id`.<fk table='characters' column='id'/>",
                  "format": "integer"
                },
                "original_text": {
                  "type": "string",
                  "format": "text"
                },
                "modern_text": {
                  "type": "string",
                  "format": "text"
                },
                "sequence": {
                  "type": "integer",
                  "format": "integer"
                }
              }
            }
          }
        },
        "required": false
      },
      "body.scenes": {
        "description": "scenes",
        "content": {
          "application/json": {
            "schema": {
              "required": [
                "id",
                "number"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "act_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `acts.id`.<fk table='acts' column='id'/>",
                  "format": "integer"
                },
                "number": {
                  "type": "integer",
                  "format": "integer"
                },
                "title": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                },
                "location": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                }
              }
            }
          },
          "application/vnd.pgrst.object+json;nulls=stripped": {
            "schema": {
              "required": [
                "id",
                "number"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "act_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `acts.id`.<fk table='acts' column='id'/>",
                  "format": "integer"
                },
                "number": {
                  "type": "integer",
                  "format": "integer"
                },
                "title": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                },
                "location": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                }
              }
            }
          },
          "application/vnd.pgrst.object+json": {
            "schema": {
              "required": [
                "id",
                "number"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "act_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `acts.id`.<fk table='acts' column='id'/>",
                  "format": "integer"
                },
                "number": {
                  "type": "integer",
                  "format": "integer"
                },
                "title": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                },
                "location": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                }
              }
            }
          },
          "text/csv": {
            "schema": {
              "required": [
                "id",
                "number"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "act_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `acts.id`.<fk table='acts' column='id'/>",
                  "format": "integer"
                },
                "number": {
                  "type": "integer",
                  "format": "integer"
                },
                "title": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                },
                "location": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                }
              }
            }
          }
        },
        "required": false
      },
      "body.acts": {
        "description": "acts",
        "content": {
          "application/json": {
            "schema": {
              "required": [
                "id",
                "number"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "play_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                  "format": "integer"
                },
                "number": {
                  "type": "integer",
                  "format": "integer"
                },
                "title": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                }
              }
            }
          },
          "application/vnd.pgrst.object+json;nulls=stripped": {
            "schema": {
              "required": [
                "id",
                "number"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "play_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                  "format": "integer"
                },
                "number": {
                  "type": "integer",
                  "format": "integer"
                },
                "title": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                }
              }
            }
          },
          "application/vnd.pgrst.object+json": {
            "schema": {
              "required": [
                "id",
                "number"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "play_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                  "format": "integer"
                },
                "number": {
                  "type": "integer",
                  "format": "integer"
                },
                "title": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                }
              }
            }
          },
          "text/csv": {
            "schema": {
              "required": [
                "id",
                "number"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "play_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                  "format": "integer"
                },
                "number": {
                  "type": "integer",
                  "format": "integer"
                },
                "title": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                }
              }
            }
          }
        },
        "required": false
      },
      "body.characters": {
        "description": "characters",
        "content": {
          "application/json": {
            "schema": {
              "required": [
                "id",
                "name"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "play_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                  "format": "integer"
                },
                "name": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                },
                "description": {
                  "type": "string",
                  "format": "text"
                }
              }
            }
          },
          "application/vnd.pgrst.object+json;nulls=stripped": {
            "schema": {
              "required": [
                "id",
                "name"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "play_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                  "format": "integer"
                },
                "name": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                },
                "description": {
                  "type": "string",
                  "format": "text"
                }
              }
            }
          },
          "application/vnd.pgrst.object+json": {
            "schema": {
              "required": [
                "id",
                "name"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "play_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                  "format": "integer"
                },
                "name": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                },
                "description": {
                  "type": "string",
                  "format": "text"
                }
              }
            }
          },
          "text/csv": {
            "schema": {
              "required": [
                "id",
                "name"
              ],
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Primary Key.<pk/>",
                  "format": "integer"
                },
                "play_id": {
                  "type": "integer",
                  "description": "Note:\nThis is a Foreign Key to `plays.id`.<fk table='plays' column='id'/>",
                  "format": "integer"
                },
                "name": {
                  "maxLength": 255,
                  "type": "string",
                  "format": "character varying"
                },
                "description": {
                  "type": "string",
                  "format": "text"
                }
              }
            }
          }
        },
        "required": false
      }
    }
  },
  "x-original-swagger-version": "2.0"
}

```

