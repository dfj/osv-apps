from osv.modules import api

api.require('java')

default = api.run("--cwd=/opendaylight /java.so -Dfelix.fileinstall.filter=^(?!org.opendaylight.(openflowplugin|openflowjava)).* -Djava.io.tmpdir=/opendaylight/work/tmp -Dosgi.install.area=/opendaylight -Dosgi.configuration.area=/opendaylight/configuration -Dosgi.frameworkClassPath=file:/opendaylight/lib/org.eclipse.osgi-3.8.1.v20120830-144521.jar,file:/opendaylight/lib/org.eclipse.virgo.kernel.equinox.extensions-3.6.0.RELEASE.jar,file:/opendaylight/lib/org.eclipse.equinox.launcher-1.3.0.v20120522-1813.jar -Dosgi.framework=file:/opendaylight/lib/org.eclipse.osgi-3.8.1.v20120830-144521.jar -Djava.awt.headless=true -classpath /opendaylight/lib/org.eclipse.osgi-3.8.1.v20120830-144521.jar:/opendaylight/lib/org.eclipse.virgo.kernel.equinox.extensions-3.6.0.RELEASE.jar:/opendaylight/lib/org.eclipse.equinox.launcher-1.3.0.v20120522-1813.jar org.eclipse.equinox.launcher.Main -console -consoleLog")
