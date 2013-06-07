from validators import validate_packaged_app, validate_manfest
from submission import submit_packaged_app

test_manifest = "ibaskethtml5.ludei.com/manifest.webapp"

#=====================================
#          MANIFEST VALIDATOR        #
#=====================================

print "Validating manifest: %s" % test_manifest
if validate_manfest(test_manifest):
    print "Validation status", "." * 20, "[OK]"
else:
    print "Validation status", "." * 20, "[FAIL]"
print

#=====================================
#        PACKAGED APP VALIDATOR      #
#=====================================

print "Validating packaged app:"
upload_id, validated = validate_packaged_app()
if validated:
    print "Validation status", "." * 20, "[OK]"
else:
    print "Validation status", "." * 20, "[FAIL]"


#====================================
#           UPLOAD APP              #
#====================================

submit_packaged_app(None, upload_id)
