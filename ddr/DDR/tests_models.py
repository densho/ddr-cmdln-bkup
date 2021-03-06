from datetime import datetime
import os

import models


def test_file_hash():
    path = '/tmp/test-hash-%s' % datetime.now().strftime('%Y%m%dT%H%M%S')
    text = 'hash'
    sha1 = '2346ad27d7568ba9896f1b7da6b5991251debdf2'
    sha256 = 'd04b98f48e8f8bcc15c6ae5ac050801cd6dcfd428fb5f9e65c4e16e7807340fa'
    md5 = '0800fc577294c34e0b28ad2839435945'
    with open(path, 'w') as f:
        f.write(text)
    assert models.file_hash(path, 'sha1') == sha1
    assert models.file_hash(path, 'sha256') == sha256
    assert models.file_hash(path, 'md5') == md5
    os.remove(path)

def test_metadata_files():
    basedir = '/tmp'
    cachedir = '.metadata_files'
    cache_path = os.path.join(basedir, cachedir)
    if os.path.exists(cache_path):
        os.remove(cache_path)
    assert not os.path.exists(cache_path)
    paths0 = models.metadata_files('/tmp', recursive=True, force_read=True, save=True)
    print('paths: %s' % paths0)
    assert os.path.exists(cache_path)
    paths1 = models.metadata_files('/tmp', recursive=True, force_read=True, save=True)
    print('paths: %s' % paths1)

def test_dissect_path():
    c0 = models.dissect_path('/base/ddr-test-123/collection.json')
    c1 = models.dissect_path('/base/ddr-test-123')
    assert c0
    assert c1
    assert c0.base_path == c1.base_path
    assert c0.collection_path == c1.collection_path
    assert c0.entity_path == c1.entity_path
    assert c0.object_type == c1.object_type
    assert c0.object_id == c1.object_id
    assert c0.repo == c1.repo
    assert c0.org == c1.org
    assert c0.cid == c1.cid
    assert c0.eid == c1.eid
    assert c0.base_path == '/base'
    assert c0.collection_path == '/base/ddr-test-123'
    assert c0.object_type == 'collection'
    assert c0.object_id == 'ddr-test-123'
    assert c0.repo == 'ddr'
    assert c0.org == 'test'
    assert c0.cid == '123'
    assert c0.eid == None
    assert c0.role == None
    assert c0.sha1 == None
    assert c0.file_id == None
    assert c0.entity_id == None
    assert c0.collection_id == 'ddr-test-123'
    
    e0 = models.dissect_path('/base/ddr-test-123/files/ddr-test-123-1/entity.json')
    e1 = models.dissect_path('/base/ddr-test-123/files/ddr-test-123-1/files')
    e2 = models.dissect_path('/base/ddr-test-123/files/ddr-test-123-1')
    assert e0
    assert e1
    assert e2
    assert e0.base_path == e1.base_path == e2.base_path
    assert e0.collection_path == e1.collection_path == e2.collection_path
    assert e0.entity_path == e1.entity_path == e2.entity_path
    assert e0.object_type == e1.object_type == e2.object_type
    assert e0.object_id == e1.object_id == e2.object_id
    assert e0.repo == e1.repo == e2.repo
    assert e0.org == e1.org == e2.org
    assert e0.cid == e1.cid == e2.cid
    assert e0.eid == e1.eid == e2.eid
    assert e0.base_path == '/base'
    assert e0.collection_path == '/base/ddr-test-123'
    assert e0.entity_path == '/base/ddr-test-123/files/ddr-test-123-1'
    assert e0.object_type == 'entity'
    assert e0.object_id == 'ddr-test-123-1'
    assert e0.repo == 'ddr'
    assert e0.org == 'test'
    assert e0.cid == '123'
    assert e0.eid == '1'
    assert e0.role == None
    assert e0.sha1 == None
    assert e0.file_id == None
    assert e0.entity_id == 'ddr-test-123-1'
    assert e0.collection_id == 'ddr-test-123'
    
    f0 = models.dissect_path('/base/ddr-test-123/files/ddr-test-123-1/files/ddr-test-123-1-master-abc-a.jpg')
    f1 = models.dissect_path('/base/ddr-test-123/files/ddr-test-123-1/files/ddr-test-123-1-master-abc.json')
    f2 = models.dissect_path('/base/ddr-test-123/files/ddr-test-123-1/files/ddr-test-123-1-master-abc.jpg')
    f3 = models.dissect_path('/base/ddr-test-123/files/ddr-test-123-1/files/ddr-test-123-1-master-abc.pdf')
    f4 = models.dissect_path('/base/ddr-test-123/files/ddr-test-123-1/files/ddr-test-123-1-master-abc')
    assert f0
    assert f1
    assert f2
    assert f3
    assert f4
    assert f0.base_path == f1.base_path == f2.base_path == f3.base_path == f4.base_path
    assert f0.collection_path == f1.collection_path == f2.collection_path == f3.collection_path == f4.collection_path
    assert f0.entity_path == f1.entity_path == f2.entity_path == f3.entity_path == f4.entity_path
    assert f0.object_type == f1.object_type == f2.object_type == f3.object_type == f4.object_type
    assert f0.object_id == f1.object_id == f2.object_id == f3.object_id == f4.object_id
    assert f0.repo == f1.repo == f2.repo == f3.repo == f4.repo
    assert f0.org == f1.org == f2.org == f3.org == f4.org
    assert f0.cid == f1.cid == f2.cid == f3.cid == f4.cid
    assert f0.eid == f1.eid == f2.eid == f3.eid == f4.eid
    assert f0.role == f1.role == f2.role == f3.role == f4.role
    assert f0.sha1 == f1.sha1 == f2.sha1 == f3.sha1 == f4.sha1
    assert f0.base_path == '/base'
    assert f0.collection_path == '/base/ddr-test-123'
    assert f0.entity_path == '/base/ddr-test-123/files/ddr-test-123-1'
    assert f0.object_type == 'file'
    assert f0.object_id == 'ddr-test-123-1-master-abc'
    assert f0.repo == 'ddr'
    assert f0.org == 'test'
    assert f0.cid == '123'
    assert f0.eid == '1'
    assert f0.role == 'master'
    assert f0.sha1 == 'abc'
    assert f0.file_id == 'ddr-test-123-1-master-abc'
    assert f0.entity_id == 'ddr-test-123-1'
    assert f0.collection_id == 'ddr-test-123'

def test_make_object_id():
    assert models.make_object_id('file','ddr','test','123','1','role','a1') == 'ddr-test-123-1-role-a1'
    assert models.make_object_id('entity','ddr','test','123','1') == 'ddr-test-123-1'
    assert models.make_object_id('collection','ddr','test','123') == 'ddr-test-123'
    assert models.make_object_id('organization','ddr','test') == 'ddr-test'
    assert models.make_object_id('org','ddr','test') == 'ddr-test'
    assert models.make_object_id('repository','ddr') == 'ddr'
    assert models.make_object_id('repo','ddr') == 'ddr'
    # edge cases
    assert models.make_object_id('repo','ddr','test','123','1','role','a1') == 'ddr'
    # mistakes
    assert models.make_object_id('file','ddr') == None
    assert models.make_object_id('badmodel','ddr','test','123','1','role','a1') == None

def test_split_object_id():
    assert models.split_object_id('ddr-test-123-1-role-a1') == ['file', 'ddr','test','123','1','role','a1']
    assert models.split_object_id('ddr-test-123-1') == ['entity', 'ddr','test','123','1']
    assert models.split_object_id('ddr-test-123') == ['collection', 'ddr','test','123']
    assert models.split_object_id('ddr-test-123-1-role-a1-xx') == None
    assert models.split_object_id('ddr-test-123-1-role') == None
    assert models.split_object_id('ddr-test') == None
    assert models.split_object_id('ddr') == None

def test_id_from_path():
    assert models.id_from_path('.../ddr-testing-123/collection.json') == 'ddr-testing-123'
    assert models.id_from_path('.../ddr-testing-123-1/entity.json') == 'ddr-testing-123-1'
    assert models.id_from_path('.../ddr-testing-123-1-master-a1.json') == 'ddr-testing-123-1-master-a1'
    assert models.id_from_path('.../ddr-testing-123/files/ddr-testing-123-1/') ==  None
    assert models.id_from_path('.../ddr-testing-123/something-else.json') ==  None

MODELFROMDICT_NOID = {}
MODELFROMDICT_FILE = {'path_rel':'this/is/a/path'}
MODELFROMDICT_ENTITY = {'id': 'ddr-test-123-1'}
MODELFROMDICT_COLL = {'id': 'ddr-test-123'}
MODELFROMDICT_ORG = {'id': 'ddr-test'}
MODELFROMDICT_REPO = {'id': 'ddr'}

def test_model_from_dict():
    assert models.model_from_dict(MODELFROMDICT_NOID) == None
    assert models.model_from_dict(MODELFROMDICT_FILE) == 'file'
    assert models.model_from_dict(MODELFROMDICT_ENTITY) == 'entity'
    assert models.model_from_dict(MODELFROMDICT_COLL) == 'collection'
    assert models.model_from_dict(MODELFROMDICT_ORG) == None
    assert models.model_from_dict(MODELFROMDICT_REPO) == None

def test_model_from_path():
    assert models.model_from_path('.../ddr-testing-123/collection.json') == 'collection'
    assert models.model_from_path('.../ddr-testing-123-1/entity.json') == 'entity'
    assert models.model_from_path('.../ddr-testing-123-1-master-a1b2c3d4e5.json') == 'file'

def test_parent_id():
    assert models.parent_id('ddr') == None
    assert models.parent_id('ddr-testing') == 'ddr'
    assert models.parent_id('ddr-testing-123') == 'ddr-testing'
    assert models.parent_id('ddr-testing-123-1') == 'ddr-testing-123'
    assert models.parent_id('ddr-testing-123-1-master-a1b2c3d4e5') == 'ddr-testing-123-1'

# TODO model_fields

def test_module_function():
    module = models
    functionname = 'id_from_path'
    value = '.../ddr-test-123/collection.json'
    assert models.module_function(module, functionname, value) == 'ddr-test-123'

# TODO module_xml_function

def test_write_json():
    data = {'a':1, 'b':2}
    path = '/tmp/ddrlocal.models.write_json.json'
    models.write_json(data, path)
    with open(path, 'r') as f:
        written = f.readlines()
    assert written == ['{\n', '    "a": 1,\n', '    "b": 2\n', '}']
    # clean up
    os.remove(path)

MODEL_FIELDS_INHERITABLE = [
    {'name':'id',},
    {'name':'record_created',},
    {'name':'record_lastmod',},
    {'name':'status', 'inheritable':True,},
    {'name':'public', 'inheritable':True,},
    {'name':'title',},
]
def test_inheritable_fields():
    assert models._inheritable_fields(MODEL_FIELDS_INHERITABLE) == ['status','public']

# TODO _inherit

# lock
# unlock
# locked
def test_locking():
    lock_path = '/tmp/test-lock-%s' % datetime.now().strftime('%Y%m%dT%H%M%S')
    text = 'we are locked. go away.'
    # before locking
    assert models.locked(lock_path) == False
    assert models.unlock(lock_path, text) == 'not locked'
    # locking
    assert models.lock(lock_path, text) == 'ok'
    # locked
    assert models.locked(lock_path) == text
    assert models.lock(lock_path, text) == 'locked'
    assert models.unlock(lock_path, 'not the right text') == 'miss'
    # unlocking
    assert models.unlock(lock_path, text) == 'ok'
    # unlocked
    assert models.locked(lock_path) == False
    assert models.unlock(lock_path, text) == 'not locked'
    assert not os.path.exists(lock_path)

def test_Collection__init__():
    c = models.Collection('/tmp/ddr-testing-123')
    assert c.path == '/tmp/ddr-testing-123'
    assert c.path_rel == 'ddr-testing-123'
    assert c.root == '/tmp'
    assert c.uid == 'ddr-testing-123'
    assert c.annex_path == '/tmp/ddr-testing-123/.git/annex'
    assert c.annex_path_rel == '.git/annex'
    assert c.changelog_path == '/tmp/ddr-testing-123/changelog'
    assert c.control_path == '/tmp/ddr-testing-123/control'
    assert c.files_path == '/tmp/ddr-testing-123/files'
    assert c.lock_path == '/tmp/ddr-testing-123/lock'
    assert c.gitignore_path == '/tmp/ddr-testing-123/.gitignore'
    assert c.changelog_path_rel == 'changelog'
    assert c.control_path_rel == 'control'
    assert c.files_path_rel == 'files'
    assert c.gitignore_path_rel == '.gitignore'
    # TODO assert c.git_url

def test_Collection_path_absrel():
    c = models.Collection('/tmp/ddr-testing-123')
    assert c._path_absrel('path/to/file') == '/tmp/ddr-testing-123/path/to/file'
    assert c._path_absrel('path/to/file', rel=True) == 'path/to/file'

def test_Collection_entity_path():
    c = models.Collection('/tmp/ddr-testing-123')
    assert c.entity_path('11') == '/tmp/ddr-testing-123/files/11'

def test_Collection_changelog():
    c = models.Collection('/tmp/ddr-testing-123')
    assert c.changelog() == '/tmp/ddr-testing-123/changelog is empty or missing'
    # TODO test reading changelog

# TODO Collection.control
# TODO Collection.gitignore
# TODO Collection.collections
# TODO Collection.entities
# TODO Collection.repo_fetch
# TODO Collection.repo_status
# TODO Collection.repo_synced
# TODO Collection.repo_ahead
# TODO Collection.repo_behind
# TODO Collection.repo_diverged
# TODO Collection.repo_conflicted
# TODO Collection.repo_annex_status

# Collection.locking
# Collection.unlock
# Collection.locked
def test_Collection_locking():
    c = models.Collection('/tmp/ddr-testing-123')
    text = 'we are locked. go away.'
    os.mkdir(c.path)
    # before locking
    assert models.locked(c.lock_path) == False
    assert models.unlock(c.lock_path, text) == 'not locked'
    # locking
    assert models.lock(c.lock_path, text) == 'ok'
    # locked
    assert models.locked(c.lock_path) == text
    assert models.lock(c.lock_path, text) == 'locked'
    assert models.unlock(c.lock_path, 'not the right text') == 'miss'
    # unlocking
    assert models.unlock(c.lock_path, text) == 'ok'
    # unlocked
    assert models.locked(c.lock_path) == False
    assert models.unlock(c.lock_path, text) == 'not locked'
    assert not os.path.exists(c.lock_path)
    os.rmdir(c.path)

def test_Entity__init__():
    e = models.Entity('/tmp/ddr-testing-123/files/1')
    assert e.path == '/tmp/ddr-testing-123/files/1'
    assert e.path_rel == 'ddr-testing-123/files/1'
    assert e.root == '/tmp'
    assert e.parent_path == '/tmp/ddr-testing-123'
    assert e.uid == '1'
    assert e.parent_uid == 'ddr-testing-123'
    assert e.lock_path == '/tmp/ddr-testing-123/files/1/lock'
    assert e.changelog_path == '/tmp/ddr-testing-123/files/1/changelog'
    assert e.control_path == '/tmp/ddr-testing-123/files/1/control'
    assert e.files_path == '/tmp/ddr-testing-123/files/1/files'
    assert e.changelog_path_rel == 'files/1/changelog'
    assert e.control_path_rel == 'files/1/control'
    assert e.files_path_rel == 'files/1/files'

def test_Entity_path_absrel():
    e = models.Entity('/tmp/ddr-testing-123/files/1')
    assert e._path_absrel('filename') == '/tmp/ddr-testing-123/files/1/filename'
    assert e._path_absrel('filename', rel=True) == 'files/1/filename'

# Entity.locking
# Entity.unlock
# Entity.locked
def test_Entity_locking():
    e = models.Entity('/tmp/ddr-testing-123-1')
    text = 'we are locked. go away.'
    os.mkdir(e.path)
    # before locking
    assert models.locked(e.lock_path) == False
    assert models.unlock(e.lock_path, text) == 'not locked'
    # locking
    assert models.lock(e.lock_path, text) == 'ok'
    # locked
    assert models.locked(e.lock_path) == text
    assert models.lock(e.lock_path, text) == 'locked'
    assert models.unlock(e.lock_path, 'not the right text') == 'miss'
    # unlocking
    assert models.unlock(e.lock_path, text) == 'ok'
    # unlocked
    assert models.locked(e.lock_path) == False
    assert models.unlock(e.lock_path, text) == 'not locked'
    assert not os.path.exists(e.lock_path)
    os.rmdir(e.path)

def test_Entity_changelog():
    e = models.Entity('/tmp/ddr-testing-123/files/1')
    assert e.changelog() == '/tmp/ddr-testing-123/files/1/changelog is empty or missing'
    # TODO test reading changelog

# TODO Entity.control
# TODO Entity.files
def test_Entity_checksum_algorithms():
    assert models.Entity.checksum_algorithms() == ['md5', 'sha1', 'sha256']

# TODO Entity.checksums

# TODO File.*
