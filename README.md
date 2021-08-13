# LO_VLQ_PrivateSamples

```


curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/B2G-RunIIWinter15wmLHE-00235 --retry 3 --create-dirs -o Configuration/GenProduction/python/B2G-RunIIWinter15wmLHE-00235-fragment.py
[ -s Configuration/GenProduction/python/B2G-RunIIWinter15wmLHE-00235-fragment.py ] 

cmsDriver.py Configuration/GenProduction/python/B2G-RunIIWinter15wmLHE-00235-fragment.py --python_filename LO_old_VLQ_custom_python_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN,LHE --fileout file:LO_old_VLQ_custom.root --conditions 106X_mcRun2_asymptotic_v13 --beamspot Realistic25ns13TeV2016Collision --step LHE,GEN --geometry DB:Extended --era Run2_2016 --no_exec --mc -n 100

cmsDriver.py  --python_filename LO_old_VLQ_custom_SIM_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:LO_old_VLQ_custom_SIM.root --conditions 106X_mcRun2_asymptotic_v13 --beamspot Realistic25ns13TeV2016Collision --step SIM --geometry DB:Extended --filein file:LO_old_VLQ_custom.root --era Run2_2016 --runUnscheduled --no_exec --mc -n 100

```
