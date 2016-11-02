## CHANGELOG

### v1.2.1 (2016-11-02)

**Fixes**

* missing source_id field for Leads added (IR-2944)

### v1.2.0 (2016-07-24)

**Features and Improvements**

* Add decimal deal value support [#9](https://github.com/basecrm/basecrm-python/pull/9)
* **Important** Deal values are now a Decimal [#9](https://github.com/basecrm/basecrm-python/pull/9)

### v1.1.1 (2016-02-10)

**Features and Improvements**

* Allow to update `source_id` on leads [#6](https://github.com/basecrm/basecrm-python/pull/6)
* Allow to update `estimated_close_date` on deals [#7](https://github.com/basecrm/basecrm-python/pull/7)

### v1.1.0 (2015-06-01)

**Features and Improvements**

* `basecrm.HttpClient` methods accept two optional parameters: `headers` and `raw`
* Sync API support
  * Low-level interface via `basecrm.SyncService`
  * High-level interface via `basecrm.Sync`

**Fixes**

* Fix to github issue #3 - "`pip install basecrm` is broken"

### v1.0.3 (2015-05-01)

**Features and Improvements**

* Make tests compatible with Python 2.6
* Make the wrapper works with Python 3 (3.2, 3.3, 3.4)
* Bunch replaced with Munch (active fork of Bunch, compatible with Python 3)

### v1.0.2 (2015-04-30)

**Features and Improvements**

* Sending proper User-Agent http header

### v1.0.1 (2015-04-25)

* Birth!
