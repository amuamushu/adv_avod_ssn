# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: avod/protos/model.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from avod.protos import layers_pb2 as avod_dot_protos_dot_layers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='avod/protos/model.proto',
  package='avod.protos',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17\x61vod/protos/model.proto\x12\x0b\x61vod.protos\x1a\x18\x61vod/protos/layers.proto\"\xbf\x04\n\x0bModelConfig\x12\x1e\n\nmodel_name\x18\x01 \x01(\t:\navod_model\x12(\n\x0f\x63heckpoint_name\x18\x02 \x01(\t:\x0f\x64\x65tection_model\x12.\n\x0cpaths_config\x18\x03 \x01(\x0b\x32\x18.avod.protos.PathsConfig\x12.\n\x0cinput_config\x18\x04 \x02(\x0b\x32\x18.avod.protos.InputConfig\x12*\n\nrpn_config\x18\x05 \x02(\x0b\x32\x16.avod.protos.RpnConfig\x12,\n\x0b\x61vod_config\x18\x06 \x02(\x0b\x32\x17.avod.protos.AvodConfig\x12\x1f\n\x17label_smoothing_epsilon\x18\x07 \x02(\x02\x12\x1b\n\x13\x65xpand_proposals_xz\x18\x08 \x02(\x02\x12\x1f\n\x17path_drop_probabilities\x18\t \x03(\x02\x12\x1c\n\x14train_on_all_samples\x18\n \x02(\x08\x12\x18\n\x10\x65val_all_samples\x18\x0b \x02(\x08\x12\x30\n\rlayers_config\x18\x0c \x02(\x0b\x32\x19.avod.protos.LayersConfig\x12,\n\x0bloss_config\x18\r \x02(\x0b\x32\x17.avod.protos.LossConfig\x12\x1d\n\x0eis_adversarial\x18\x0e \x01(\x08:\x05\x66\x61lse\x12\x16\n\x0b\x61\x64v_epsilon\x18\x0f \x01(\x02:\x01\x30\"G\n\x0bPathsConfig\x12\x16\n\x0e\x63heckpoint_dir\x18\x01 \x01(\t\x12\x0e\n\x06logdir\x18\x02 \x01(\t\x12\x10\n\x08pred_dir\x18\x03 \x01(\t\"\x9e\x01\n\x0bInputConfig\x12\x17\n\nbev_dims_h\x18\x01 \x01(\x05:\x03\x37\x30\x30\x12\x17\n\nbev_dims_w\x18\x02 \x01(\x05:\x03\x38\x30\x30\x12\x14\n\tbev_depth\x18\x03 \x01(\x05:\x01\x36\x12\x17\n\nimg_dims_h\x18\x04 \x01(\x05:\x03\x34\x38\x30\x12\x18\n\nimg_dims_w\x18\x05 \x01(\x05:\x04\x31\x35\x39\x30\x12\x14\n\timg_depth\x18\x06 \x01(\x05:\x01\x33\"\x9d\x01\n\tRpnConfig\x12\"\n\x1arpn_proposal_roi_crop_size\x18\x01 \x02(\x05\x12\x19\n\x11rpn_fusion_method\x18\x02 \x02(\t\x12\x1a\n\x12rpn_train_nms_size\x18\x03 \x02(\x05\x12\x19\n\x11rpn_test_nms_size\x18\x04 \x02(\x05\x12\x1a\n\x12rpn_nms_iou_thresh\x18\x05 \x02(\x02\"\xa7\x01\n\nAvodConfig\x12#\n\x1b\x61vod_proposal_roi_crop_size\x18\x01 \x02(\x05\x12\x1f\n\x17\x61vod_positive_selection\x18\x03 \x02(\t\x12\x15\n\ravod_nms_size\x18\x04 \x02(\x05\x12\x1b\n\x13\x61vod_nms_iou_thresh\x18\x05 \x02(\x02\x12\x1f\n\x17\x61vod_box_representation\x18\x06 \x02(\t\"W\n\nLossConfig\x12\x17\n\x0freg_loss_weight\x18\x01 \x02(\x02\x12\x17\n\x0f\x61ng_loss_weight\x18\x02 \x02(\x02\x12\x17\n\x0f\x63ls_loss_weight\x18\x03 \x02(\x02'
  ,
  dependencies=[avod_dot_protos_dot_layers__pb2.DESCRIPTOR,])




_MODELCONFIG = _descriptor.Descriptor(
  name='ModelConfig',
  full_name='avod.protos.ModelConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_name', full_name='avod.protos.ModelConfig.model_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"avod_model".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='checkpoint_name', full_name='avod.protos.ModelConfig.checkpoint_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"detection_model".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paths_config', full_name='avod.protos.ModelConfig.paths_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input_config', full_name='avod.protos.ModelConfig.input_config', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rpn_config', full_name='avod.protos.ModelConfig.rpn_config', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avod_config', full_name='avod.protos.ModelConfig.avod_config', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label_smoothing_epsilon', full_name='avod.protos.ModelConfig.label_smoothing_epsilon', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expand_proposals_xz', full_name='avod.protos.ModelConfig.expand_proposals_xz', index=7,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path_drop_probabilities', full_name='avod.protos.ModelConfig.path_drop_probabilities', index=8,
      number=9, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='train_on_all_samples', full_name='avod.protos.ModelConfig.train_on_all_samples', index=9,
      number=10, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eval_all_samples', full_name='avod.protos.ModelConfig.eval_all_samples', index=10,
      number=11, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='layers_config', full_name='avod.protos.ModelConfig.layers_config', index=11,
      number=12, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loss_config', full_name='avod.protos.ModelConfig.loss_config', index=12,
      number=13, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_adversarial', full_name='avod.protos.ModelConfig.is_adversarial', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adv_epsilon', full_name='avod.protos.ModelConfig.adv_epsilon', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=642,
)


_PATHSCONFIG = _descriptor.Descriptor(
  name='PathsConfig',
  full_name='avod.protos.PathsConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='checkpoint_dir', full_name='avod.protos.PathsConfig.checkpoint_dir', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logdir', full_name='avod.protos.PathsConfig.logdir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pred_dir', full_name='avod.protos.PathsConfig.pred_dir', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=644,
  serialized_end=715,
)


_INPUTCONFIG = _descriptor.Descriptor(
  name='InputConfig',
  full_name='avod.protos.InputConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bev_dims_h', full_name='avod.protos.InputConfig.bev_dims_h', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=700,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bev_dims_w', full_name='avod.protos.InputConfig.bev_dims_w', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=800,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bev_depth', full_name='avod.protos.InputConfig.bev_depth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=6,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='img_dims_h', full_name='avod.protos.InputConfig.img_dims_h', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=480,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='img_dims_w', full_name='avod.protos.InputConfig.img_dims_w', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1590,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='img_depth', full_name='avod.protos.InputConfig.img_depth', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=718,
  serialized_end=876,
)


_RPNCONFIG = _descriptor.Descriptor(
  name='RpnConfig',
  full_name='avod.protos.RpnConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rpn_proposal_roi_crop_size', full_name='avod.protos.RpnConfig.rpn_proposal_roi_crop_size', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rpn_fusion_method', full_name='avod.protos.RpnConfig.rpn_fusion_method', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rpn_train_nms_size', full_name='avod.protos.RpnConfig.rpn_train_nms_size', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rpn_test_nms_size', full_name='avod.protos.RpnConfig.rpn_test_nms_size', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rpn_nms_iou_thresh', full_name='avod.protos.RpnConfig.rpn_nms_iou_thresh', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=879,
  serialized_end=1036,
)


_AVODCONFIG = _descriptor.Descriptor(
  name='AvodConfig',
  full_name='avod.protos.AvodConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='avod_proposal_roi_crop_size', full_name='avod.protos.AvodConfig.avod_proposal_roi_crop_size', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avod_positive_selection', full_name='avod.protos.AvodConfig.avod_positive_selection', index=1,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avod_nms_size', full_name='avod.protos.AvodConfig.avod_nms_size', index=2,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avod_nms_iou_thresh', full_name='avod.protos.AvodConfig.avod_nms_iou_thresh', index=3,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avod_box_representation', full_name='avod.protos.AvodConfig.avod_box_representation', index=4,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1039,
  serialized_end=1206,
)


_LOSSCONFIG = _descriptor.Descriptor(
  name='LossConfig',
  full_name='avod.protos.LossConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reg_loss_weight', full_name='avod.protos.LossConfig.reg_loss_weight', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ang_loss_weight', full_name='avod.protos.LossConfig.ang_loss_weight', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cls_loss_weight', full_name='avod.protos.LossConfig.cls_loss_weight', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1208,
  serialized_end=1295,
)

_MODELCONFIG.fields_by_name['paths_config'].message_type = _PATHSCONFIG
_MODELCONFIG.fields_by_name['input_config'].message_type = _INPUTCONFIG
_MODELCONFIG.fields_by_name['rpn_config'].message_type = _RPNCONFIG
_MODELCONFIG.fields_by_name['avod_config'].message_type = _AVODCONFIG
_MODELCONFIG.fields_by_name['layers_config'].message_type = avod_dot_protos_dot_layers__pb2._LAYERSCONFIG
_MODELCONFIG.fields_by_name['loss_config'].message_type = _LOSSCONFIG
DESCRIPTOR.message_types_by_name['ModelConfig'] = _MODELCONFIG
DESCRIPTOR.message_types_by_name['PathsConfig'] = _PATHSCONFIG
DESCRIPTOR.message_types_by_name['InputConfig'] = _INPUTCONFIG
DESCRIPTOR.message_types_by_name['RpnConfig'] = _RPNCONFIG
DESCRIPTOR.message_types_by_name['AvodConfig'] = _AVODCONFIG
DESCRIPTOR.message_types_by_name['LossConfig'] = _LOSSCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelConfig = _reflection.GeneratedProtocolMessageType('ModelConfig', (_message.Message,), {
  'DESCRIPTOR' : _MODELCONFIG,
  '__module__' : 'avod.protos.model_pb2'
  # @@protoc_insertion_point(class_scope:avod.protos.ModelConfig)
  })
_sym_db.RegisterMessage(ModelConfig)

PathsConfig = _reflection.GeneratedProtocolMessageType('PathsConfig', (_message.Message,), {
  'DESCRIPTOR' : _PATHSCONFIG,
  '__module__' : 'avod.protos.model_pb2'
  # @@protoc_insertion_point(class_scope:avod.protos.PathsConfig)
  })
_sym_db.RegisterMessage(PathsConfig)

InputConfig = _reflection.GeneratedProtocolMessageType('InputConfig', (_message.Message,), {
  'DESCRIPTOR' : _INPUTCONFIG,
  '__module__' : 'avod.protos.model_pb2'
  # @@protoc_insertion_point(class_scope:avod.protos.InputConfig)
  })
_sym_db.RegisterMessage(InputConfig)

RpnConfig = _reflection.GeneratedProtocolMessageType('RpnConfig', (_message.Message,), {
  'DESCRIPTOR' : _RPNCONFIG,
  '__module__' : 'avod.protos.model_pb2'
  # @@protoc_insertion_point(class_scope:avod.protos.RpnConfig)
  })
_sym_db.RegisterMessage(RpnConfig)

AvodConfig = _reflection.GeneratedProtocolMessageType('AvodConfig', (_message.Message,), {
  'DESCRIPTOR' : _AVODCONFIG,
  '__module__' : 'avod.protos.model_pb2'
  # @@protoc_insertion_point(class_scope:avod.protos.AvodConfig)
  })
_sym_db.RegisterMessage(AvodConfig)

LossConfig = _reflection.GeneratedProtocolMessageType('LossConfig', (_message.Message,), {
  'DESCRIPTOR' : _LOSSCONFIG,
  '__module__' : 'avod.protos.model_pb2'
  # @@protoc_insertion_point(class_scope:avod.protos.LossConfig)
  })
_sym_db.RegisterMessage(LossConfig)


# @@protoc_insertion_point(module_scope)
