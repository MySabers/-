# coding: utf-8

from elasticsearch import Elasticsearch

es = Elasticsearch("localhost:9200")

# 创建 索引 忽略400的错误
es.indices.create(index='index_name', ignore=400)

# 单挑插入数据
es.index(index='http_code_1', doc_type='error_code', id=01, body=es_dict)

# 批量插入
success, info = helpers.bulk(es, data_l, index="bulk", doc_type="doc")

# 查询数据
res = es.get(index="_index", doc_type="_type", id=01)

# 删除数据
es.delete(index="_index", doc_type="_type", id=_id)

# 删除 索引 忽略400和404的错误
es.indices.delete(index='index_name', ignore=[400, 404])

==========================================================
# 搜索所有数据
es.search(index="_index", doc_type="_type")

# 搜索所有数据
body = {
	"query":{
		"match_all":{}
	}
}

# 查询指定数据(age = 0)			term
body = {
	"query":{
		"term":{
			"age":0
		}
	}
}

# 查询指定数据(age=0 或 age=1)	terms
body = {
	"query":{
		"terms":{
			"age": [0,1]
		}
	}
}

# 匹配字段包含关键字的数据(age包含0的所有数据)		match
body = {
	"query":{
		"match":{
			"age": 0
		}
	}
}

# 查询多个字段内包含的数据
body = {
	"query":{
		"milti_match":{
			"query": 0,		# 查询关键字
			"fields": ["age", "ts"]	# 带查询字段
		}
	}
}

# 根据ID查询数据
body = {
	"query":{
		"ids":{
			"type": "_type",
			"values":["1", "2"]	# 查询ID为1或2的所有数据
		}
	}
}
es.search(index="my_index",doc_type="test_type",body=body)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 复合查询bool
body = {
	"query":{
		"bool":{
			"must":[
				{"term":{"name":"python"}},
				{"term":{"age":18}}
				# 获取name为python 并且age为18的数据
			]
		}
	}
}

# 切片式查询
body = {
	"query":{
		"match_all": {}
	}
	"from": n	# 从第n条数据开始
	"size": m	# 获取m条数据
}

# 范围查询
body = {
	"query":{
		"range":{
			"gte":18,	#>=18
			"lte":30	#<=30
		}
	}
}

# 前缀查询
body = {
	"query":{
		"prefix":{
			"name": "p"	查询前缀为p的所有数据
		}
	}
}

# 通配符查询
body = {
    "query":{
        "wildcard":{
            "name":"*id"	查询所有以id为后缀的所有数据
        }
    }
}
