import os
import stat
import logging
import subprocess
import shlex

from lib.cuckoo.common.abstracts import Auxiliary
from lib.cuckoo.common.config import Config
from lib.cuckoo.common.objects import File

log = logging.getLogger(__name__)

class YaraGen(Auxiliary):
    def start(self):
#        if "yaragen" not in self.task.options:
#            return

        genstart = self.options.get("yarGen.py", "/data/cuckoo/yarGen/yarGen.py")


            
        if not os.path.exists(genstart):
            log.error("yarGen doesnt exist at \"%s\", yarGen "
                      "disabled", genstart)
            return


        try:
            mal_path = os.path.dirname(os.path.abspath(self.task.target))
            mdma5 = File(self.task.target).get_md5()
            blat_id = str(self.task.id)




            #file_str = "/data/cuckoo/storage/analyses/%s/reports/%s.yara" % (blat_id , mdma5)
            file_str = "/data/cuckoo/storage/analyses/%s/reports/report.yara" % (blat_id)
            dir_path = os.path.dirname(file_str)

            try:
                os.stat(dir_path)
            except:
                os.makedirs(dir_path)       




            os.chdir("/data/cuckoo/yarGen/")
#            cmd_str = "python yarGen.py -m %s -o /data/cuckoo/storage/analysis/%s/reports/%s.yara -noop" % (mal_path, blat_id , mdma5)
            cmd_str = "python yarGen.py -m %s -o %s -noop" % (mal_path, file_str)
            cmd_args = shlex.split(cmd_str)
            subprocess.Popen(cmd_args)



#            cmd_str = "cd /data/cuckoo/yarGen && python yarGen.py -m %s -o /data/cuckoo/yarGen/this_should_be_changed.yara -noop" % (mal_path)
#            os.system(cmd_str)
#            cmd_args = shlex.split(cmd_str)
#            self.proc = subprocess.Popen(cmd_args , shell=True)
#            subprocess.call(pargs)

        except (OSError, ValueError):
            log.exception("Failed to start yarGen for %s", str(self.task.target))
            return

        log.info("Started yarGen for %s", str(self.task.target))

