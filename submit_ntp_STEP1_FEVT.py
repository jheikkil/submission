[Common]
mode = NTP
name = ntuples_Step1

tasks = MinBias_PU200

cmssw_config = configs/step1_L1_tree.py
version = v1
output_dir_base = /eos/cms/store/user/jheikkil/TRG_EG_study/
ncpu = 3
output_file_name = ntuple.root

[MinBias_PU200]
input_dataset = /MinBias_TuneCP5_14TeV-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/FEVT
input_directory =
crab = True
splitting_mode = Automatic
splitting_granularity = 200
job_flavor =
max_events = 20000

