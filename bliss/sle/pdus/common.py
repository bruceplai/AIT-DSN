from pyasn1.type import univ, char, namedtype, namedval, tag, constraint, useful


###############################################################################
#
# SLE Service Common Types
#
###############################################################################
class Credentials(univ.Choice):
    pass


Credentials.componentType = namedtype.NamedTypes(
    namedtype.NamedType('unused', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('used', univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 256)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))
)


class DeliveryMode(univ.Integer):
    pass


DeliveryMode.namedValues = namedval.NamedValues(
    ('rtnTimelyOnline', 0),
    ('rtnCompleteOnline', 1),
    ('rtnOffline', 2),
    ('fwdOnline', 3),
    ('fwdOffline', 4)
)


class Diagnostics(univ.Integer):
    pass


Diagnostics.namedValues = namedval.NamedValues(
    ('duplicateInvokeId', 100),
    ('otherReason', 127)
)


class IntPosLong(univ.Integer):
    pass


IntPosLong.subtypeSpec = constraint.ValueRangeConstraint(1, 4294967295)


class IntPosShort(univ.Integer):
    pass


IntPosShort.subtypeSpec = constraint.ValueRangeConstraint(1, 65535)


class IntUnsignedLong(univ.Integer):
    pass


IntUnsignedLong.subtypeSpec = constraint.ValueRangeConstraint(0, 4294967295)


class IntUnsignedShort(univ.Integer):
    pass


IntUnsignedShort.subtypeSpec = constraint.ValueRangeConstraint(0, 65535)


class Duration(IntUnsignedLong):
    pass


class ForwardDuStatus(univ.Integer):
    pass


ForwardDuStatus.namedValues = namedval.NamedValues(
    ('radiated', 0),
    ('expired', 1),
    ('interrupted', 2),
    ('acknowledged', 3),
    ('productionStarted', 4),
    ('productionNotStarted', 5),
    ('unsupportedTransmissionMode', 6)
)


class InvokeId(IntUnsignedShort):
    pass


class ParameterName(univ.Integer):
    pass


ParameterName.namedValues = namedval.NamedValues(
    ('acquisitionSequenceLength', 201),
    ('apidList', 2),
    ('bitLockRequired', 3),
    ('blockingTimeoutPeriod', 0),
    ('blockingUsage', 1),
    ('bufferSize', 4),
    ('clcwGlobalVcId', 202),
    ('clcwPhysicalChannel', 203),
    ('copCntrFramesRepetition', 300),
    ('deliveryMode', 6),
    ('directiveInvocation', 7),
    ('directiveInvocationOnline', 108),
    ('expectedDirectiveIdentification', 8),
    ('expectedEventInvocationIdentification', 9),
    ('expectedSlduIdentification', 10),
    ('fopSlidingWindow', 11),
    ('fopState', 12),
    ('latencyLimit', 15),
    ('mapList', 16),
    ('mapMuxControl', 17),
    ('mapMuxScheme', 18),
    ('maximumFrameLength', 19),
    ('maximumPacketLength', 20),
    ('maximumSlduLength', 21),
    ('minimumDelayTime', 204),
    ('minReportingCycle', 301),
    ('modulationFrequency', 22),
    ('modulationIndex', 23),
    ('notificationMode', 205),
    ('permittedControlWordTypeSet', 101),
    ('permittedFrameQuality', 302),
    ('permittedGvcidSet', 24),
    ('permittedTcVcidSet', 102),
    ('permittedTransmissionMode', 107),
    ('permittedUpdateModeSet', 103),
    ('plop1IdleSequenceLength', 206),
    ('plopInEffect', 25),
    ('protocolAbortMode', 207),
    ('reportingCycle', 26),
    ('requestedControlWordType', 104),
    ('requestedFrameQuality', 27),
    ('requestedGvcid', 28),
    ('requestedTcVcid', 105),
    ('requestedUpdateMode', 106),
    ('returnTimeoutPeriod', 29),
    ('rfAvailable', 30),
    ('rfAvailableRequired', 31),
    ('segmentHeader', 32),
    ('sequCntrFramesRepetition', 303),
    ('subcarrierToBitRateRatio', 34),
    ('throwEventOperation', 304),
    ('timeoutType', 35),
    ('timerInitial', 36),
    ('transmissionLimit', 37),
    ('transmitterFrameSequenceNumber', 38),
    ('vcMuxControl', 39),
    ('vcMuxScheme', 40),
    ('virtualChannel', 41)
)


class SlduStatusNotification(univ.Integer):
    pass


SlduStatusNotification.namedValues = namedval.NamedValues(
    ('produceNotification', 0),
    ('doNotProduceNotification', 1)
)


class SpaceLinkDataUnit(univ.OctetString):
    pass


SpaceLinkDataUnit.subtypeSpec = constraint.ValueSizeConstraint(1, 65536)


class TimeCCSDS(univ.OctetString):
    pass


TimeCCSDS.subtypeSpec = constraint.ValueSizeConstraint(8, 8)


class TimeCCSDSpico(univ.OctetString):
    pass


TimeCCSDSpico.subtypeSpec = constraint.ValueSizeConstraint(10, 10)


class Time(univ.Choice):
    pass


Time.componentType = namedtype.NamedTypes(
    namedtype.NamedType('ccsdsFormat', TimeCCSDS().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('ccsdsPicoFormat', TimeCCSDSpico().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))
)


class ConditionalTime(univ.Choice):
    pass


ConditionalTime.componentType = namedtype.NamedTypes(
    namedtype.NamedType('undefined', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('known', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))
)

###############################################################################
#
# SLE Service Common PDUS
#
###############################################################################
class DiagnosticScheduleStatusReport(univ.Choice):
    pass


DiagnosticScheduleStatusReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType('common', Diagnostics().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('specific', univ.Integer(namedValues=namedval.NamedValues(('notSupportedInThisDeliveryMode', 0), ('alreadyStopped', 1), ('invalidReportingCycle', 2))).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))
)


class ReportingCycle(univ.Integer):
    pass


ReportingCycle.subtypeSpec = constraint.ValueRangeConstraint(2, 600)


class ReportRequestType(univ.Choice):
    pass


ReportRequestType.componentType = namedtype.NamedTypes(
    namedtype.NamedType('immediately', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('periodically', ReportingCycle().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('stop', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))
)


class SleAcknowledgement(univ.Sequence):
    pass


SleAcknowledgement.componentType = namedtype.NamedTypes(
    namedtype.NamedType('credentials', Credentials()),
    namedtype.NamedType('invokeId', InvokeId()),
    namedtype.NamedType('result', univ.Choice(componentType=namedtype.NamedTypes(
        namedtype.NamedType('positiveResult', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('negativeResult', Diagnostics().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))
    ))
    )
)


class SleScheduleStatusReportInvocation(univ.Sequence):
    pass


SleScheduleStatusReportInvocation.componentType = namedtype.NamedTypes(
    namedtype.NamedType('invokerCredentials', Credentials()),
    namedtype.NamedType('invokeId', InvokeId()),
    namedtype.NamedType('reportRequestType', ReportRequestType())
)


class SleScheduleStatusReportReturn(univ.Sequence):
    pass


SleScheduleStatusReportReturn.componentType = namedtype.NamedTypes(
    namedtype.NamedType('performerCredentials', Credentials()),
    namedtype.NamedType('invokeId', InvokeId()),
    namedtype.NamedType('result', univ.Choice(componentType=namedtype.NamedTypes(
        namedtype.NamedType('positiveResult', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('negativeResult', DiagnosticScheduleStatusReport().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))
    ))
    )
)


class SleStopInvocation(univ.Sequence):
    pass


SleStopInvocation.componentType = namedtype.NamedTypes(
    namedtype.NamedType('invokerCredentials', Credentials()),
    namedtype.NamedType('invokeId', InvokeId())
)
