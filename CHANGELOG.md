## CHANGELOG

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
