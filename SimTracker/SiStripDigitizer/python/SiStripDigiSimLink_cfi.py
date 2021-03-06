import FWCore.ParameterSet.Config as cms

from CalibTracker.SiStripESProducers.SiStripGainSimESProducer_cfi import *

simSiStripDigiSimLink = cms.EDProducer("DigiSimLinkProducer",
                               #---SiLinearChargeDivider
                               DeltaProductionCut      = cms.double(0.120425),
                               APVpeakmode             = cms.bool(False), # also SiStripDigitizerAlgorithm
                               LandauFluctuations      = cms.bool(True),
                               chargeDivisionsPerStrip = cms.int32(10),
                               CosmicDelayShift        = cms.untracked.double(0.0), # also SiStripDigitizerAlgorithm
                               #---SiHitDigitizer
                               DepletionVoltage        = cms.double(170.0),
                               AppliedVoltage          = cms.double(300.0),
                               ChargeMobility          = cms.double(310.0),
                               Temperature             = cms.double(273.0),
                               GevPerElectron          = cms.double(3.61e-09),
                               ChargeDistributionRMS   = cms.double(6.5e-10),
                               noDiffusion             = cms.bool(False),
                               #---SiTrivialInduceChargeOnStrips
                               #switch to use different coupling constants set
                               #if True RunII cross talk will be used
                               #if False RunI cross talk will be used
                               CouplingConstantsRunIIDecB   = cms.bool(False), #for TIB and TOB
                               CouplingConstantsRunIIDecW   = cms.bool(False), #for TID and TEC
                               #TIB
                               CouplingConstantDecIB1  = cms.vdouble(0.7748, 0.0962,0.0165),                    
                               CouplingConstantDecIB2  = cms.vdouble(0.8300, 0.0756,0.0094),                    
                               CouplingConstantPeakIB1 = cms.vdouble(0.9006, 0.0497),                           
                               CouplingConstantPeakIB2 = cms.vdouble(0.9342, 0.0328),                           
                               #TOB
                               CouplingConstantDecOB1  = cms.vdouble(0.6871, 0.1222, 0.0342),                   
                               CouplingConstantDecOB2  = cms.vdouble(0.7250, 0.1102, 0.0273),                   
                               CouplingConstantPeakOB1 = cms.vdouble(0.8542, 0.0729),                           
                               CouplingConstantPeakOB2 = cms.vdouble(0.8719, 0.0640),
                               #TID
                               CouplingConstantDecW1a  = cms.vdouble(0.786, 0.093, 0.014),                      
                               CouplingConstantDecW2a  = cms.vdouble(0.7962, 0.0914, 0.0104),                   
                               CouplingConstantDecW3a  = cms.vdouble(0.8164, 0.0900, 0.0018),                   
                               CouplingConstantPeakW1a = cms.vdouble(0.996, 0.002),                             
                               CouplingConstantPeakW2a = cms.vdouble(1.0,   0.000),                             
                               CouplingConstantPeakW3a = cms.vdouble(0.996, 0.002),
                               #TEC
                               CouplingConstantDecW1b  = cms.vdouble(0.822, 0.08,  0.009),                      
                               CouplingConstantDecW2b  = cms.vdouble(0.888, 0.05,  0.006),                      
                               CouplingConstantDecW3b  = cms.vdouble(0.848, 0.06,  0.016),                      
                               CouplingConstantDecW4   = cms.vdouble(0.876, 0.06,  0.002),                      
                               CouplingConstantDecW5   = cms.vdouble(0.7565, 0.0913, 0.0304),                   
                               CouplingConstantDecW6   = cms.vdouble(0.758, 0.093, 0.026),                      
                               CouplingConstantDecW7   = cms.vdouble(0.7828, 0.0862, 0.0224),                   
                               CouplingConstantPeakW1b = cms.vdouble(0.976, 0.012),                             
                               CouplingConstantPeakW2b = cms.vdouble(0.998, 0.001),                             
                               CouplingConstantPeakW3b = cms.vdouble(0.992, 0.004),                             
                               CouplingConstantPeakW4  = cms.vdouble(0.992, 0.004),                             
                               CouplingConstantPeakW5  = cms.vdouble(0.968, 0.016),
                               CouplingConstantPeakW6  = cms.vdouble(0.972, 0.014),
                               CouplingConstantPeakW7  = cms.vdouble(0.964, 0.018),

                               #RunII (2018) deconvolution parameters 
                               #TIB
                               CouplingConstantRunIIDecIB1 = cms.vdouble(0.8361, 0.0703, 0.0117),
                               CouplingConstantRunIIDecIB2 = cms.vdouble(0.8616, 0.0588, 0.0104),
                               #TOB
                               CouplingConstantRunIIDecOB2 = cms.vdouble(0.7925, 0.0834, 0.0203),
                               CouplingConstantRunIIDecOB1 = cms.vdouble(0.7461, 0.0996, 0.0273),
                               #TID
                               CouplingConstantRunIIDecW1a = cms.vdouble(0.8571, 0.0608, 0.0106),
                               CouplingConstantRunIIDecW2a = cms.vdouble(0.8861, 0.049, 0.008),
                               CouplingConstantRunIIDecW3a = cms.vdouble(0.8984, 0.0494, 0.0014),
                               #TEC
                               CouplingConstantRunIIDecW1b = cms.vdouble(0.8827, 0.0518, 0.0068),
                               CouplingConstantRunIIDecW2b = cms.vdouble(0.8943, 0.0483, 0.0046),
                               CouplingConstantRunIIDecW3b = cms.vdouble(0.8611, 0.0573, 0.0121),
                               CouplingConstantRunIIDecW4  = cms.vdouble(0.8881, 0.0544, 0.0015),
                               CouplingConstantRunIIDecW5  = cms.vdouble(0.7997, 0.077, 0.0231),
                               CouplingConstantRunIIDecW6  = cms.vdouble(0.8067, 0.0769, 0.0198),
                               CouplingConstantRunIIDecW7  = cms.vdouble(0.7883, 0.0888, 0.0171),

                               #-----SiStripDigitizer
                               DigiModeList = cms.PSet(SCDigi = cms.string('ScopeMode'),
                                                       ZSDigi = cms.string('ZeroSuppressed'),
                                                       PRDigi = cms.string('ProcessedRaw'),
                                                       VRDigi = cms.string('VirginRaw')),
                               ROUList = cms.vstring("g4SimHitsTrackerHitsTIBLowTof","g4SimHitsTrackerHitsTIBHighTof",
                                                     "g4SimHitsTrackerHitsTIDLowTof","g4SimHitsTrackerHitsTIDHighTof",
                                                     "g4SimHitsTrackerHitsTOBLowTof","g4SimHitsTrackerHitsTOBHighTof",
                                                     "g4SimHitsTrackerHitsTECLowTof","g4SimHitsTrackerHitsTECHighTof"),
                               GeometryType               = cms.string('idealForDigi'),
                               TrackerConfigurationFromDB = cms.bool(False),
                               ZeroSuppression            = cms.bool(True),
                               LorentzAngle               = cms.string(''),
                               Gain                       = cms.string(''),
                               #-----SiStripDigitizerAlgorithm
                               NoiseSigmaThreshold        = cms.double(2.0),
                               electronPerAdcDec          = cms.double(247.0), #tuned on collisions at 7 TeV
                               electronPerAdcPeak         = cms.double(262.0), #tuned on craft08
                               FedAlgorithm               = cms.int32(4),
                               Noise                      = cms.bool(True), ## NOTE : turning Noise ON/OFF will make a big change
 			       #Parameters valid only if Noise = True and ZeroSuppression = False
			       RealPedestals              = cms.bool(True), #The pedestal for each stip is read from the Db. if False it is added to all the strips the cnetral strip pedestal value
			       SingleStripNoise           = cms.bool(True), #The noise RMS is read from the Db. If false it is considered the central strip noise
                               CommonModeNoise            = cms.bool(True),
                               BaselineShift              = cms.bool(True),
                               APVSaturationFromHIP       = cms.bool(True),
                               APVSaturationProb          = cms.double(0.001),
                               cmnRMStib                  = cms.double(5.92),
                               cmnRMStob                  = cms.double(1.08),
                               cmnRMStid                  = cms.double(3.08),
                               cmnRMStec                  = cms.double(2.44),
							   PedestalsOffset            = cms.double(128),
                               #
                               TOFCutForDeconvolution     = cms.double(50.0),
                               TOFCutForPeak              = cms.double(100.0),
                               Inefficiency               = cms.double(0.0)
                              )

from Configuration.Eras.Modifier_run2_common_cff import run2_common
run2_common.toModify(simSiStripDigiSimLink,
                     CouplingConstantsRunIIDecB   = cms.bool(True), #for TIB and TOB
                     CouplingConstantsRunIIDecW   = cms.bool(True)  #for TID and TEC
                     )
