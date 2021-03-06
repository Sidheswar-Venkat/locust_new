# CONFIG = {
#     'local' : {"username":"SHMSystemAdmin@operasolutions.com","password":"operaSHMQA$4"},
#     'solution_name' : "CVS_KC_PERF_QA",
#     'solution' : "CVSKCPERFQA",
#     'definition' : "score_all"
# }

CONFIG = {
    'local' : {"username":"joydeep.purkayastha@operasolutions.com","password":"operaSHMQA$4"},
    'solution_name' : "CVS_KC_PERF_QA",
    'solution' : "CVSKCPERFQA",
    'definition' : "testing_wf"
}

inputs1 = {
    "sample" : {"variant":"2017.08.09-18.06.43.718-0400",
                "clusterData":True,
                "solutionName":"CVSKCPERFQA",
                "reportName":"Script_1",
                "view":"sigout.cust_txn_sigs.card_txn_single_month_sigs",
                "columns":["xtra_card_nbr","txn_month_key","cnt_fs_cpn_trips"]
                },
    "sample2" : {"queries":[],
                "limit":50,
                "columns":["xtra_card_nbr","txn_month_key","cnt_fs_cpn_trips"],
                "offset":0,
                "aggregates":{"xtra_card_nbr":"count","txn_month_key":"count","cnt_fs_cpn_trips":"count"},
                "format":{},
                "aggregationFormat":{},
                "sort":[{"xtra_card_nbr":"asc"}]
                },
    "sample3" : {"queries":[{"GROUP":{"GROUP":"xtra_card_nbr","cnt_fs_cpn_trips":"SUM"}}],
                "limit":50,
                "columns":["xtra_card_nbr","txn_month_key","cnt_fs_cpn_trips"],
                "offset":0,
                "aggregates":{"xtra_card_nbr":"count","txn_month_key":"count","cnt_fs_cpn_trips":"count"},
                "format":{},
                "aggregationFormat":{},
                "sort":[{"xtra_card_nbr":"asc"}]
                },
    "sample4" : {"queries":[{"GROUP":{"GROUP":"xtra_card_nbr","cnt_fs_cpn_trips":"SUM"}},{"FILTER":{"cnt_fs_cpn_trips":">20"}}],
                "limit":50,"columns":["xtra_card_nbr","txn_month_key","cnt_fs_cpn_trips"],
                "offset":0,"aggregates":{"xtra_card_nbr":"count","cnt_fs_cpn_trips":"count"},
                "format":{},
                "aggregationFormat":{},
                "sort":[{"xtra_card_nbr":"asc"}]
                },
    "download" : {"queries":[{"GROUP":{"GROUP":"xtra_card_nbr","cnt_fs_cpn_trips":"SUM"}},{"FILTER":{"cnt_fs_cpn_trips":">20"}}],
                "limit":500,
                "offset":0,
                "aggregates":{"xtra_card_nbr":"count","cnt_fs_cpn_trips":"count"},
                "dateFormat":"yyyy-MM-d",
                "decimalFormat":"#,##"
                },
    "name_value2" : "household",
    "name_value1" : "segmentation",
    "name_value8" : "segment_dsc",
    "fqn_1" : "listpull.welcome.step_3",
    "fqn_2" : "sigout.hh_sigs.hh_sigs_1",
    "fqn_3" : "sigout.hh_sigs.hh_sigs",
    "fqn_4" : "dim.customer.customer_segment_dim.customer_segment_dim",
    "name_value7" : "past 1 rolling month",
    "name_value6" : "count",
    "name_value9" : "cnt_fs_trips_p30d",
    "name_value10" : "hh_sigs",
    "name_value11" : "cnt_fs_cpn_trips",
    "report" : "report-1503433837090",
    "script" : "Script_1",
    "value_1" : "sigout.cust_txn_sigs.card_txn_single_month_sigs",
    "name_value3" : "customer_segment_dim_coll",
    "name_value4" : "step_3",
    "name_value5" : "hh_sigs_1",
    "fqn_value1" : "dim.customer.customer_segment_dim.customer_segment_dim_coll",
    "fqn_value2" : "dim.customer.customer_segment_dim.customer_segment_dim",
    "fqn_value3" : "listpull.welcome.base_pop_QC",
    "fqn_value4" : "listpull.welcome.step_3",
    "fqn_value5" : "listpull.ob_dynamic.low_e_pop",
    "fqn_value6" : "listpull.listpull_reports.basket_builder",
    "fqn_value" : "listpull.promo_targeting.promo_targeting",
    "fqn_value7" : "sigout.hh_sigs.hh_sigs_1",
    "fqn_value8" : "sigout.hh_sigs.hh_sigs",
    "signal_name1" : "Segment description of the customer",
    "signal_name2" : "Segment number of the customer",
    "explorer" : "USE CASE EXPLORER",
    "datalayer_name" : "List Pull - Promo Targeting",
    "search" : "promo",
    "signal_set_name" : "card_txn_single_month_sigs"
}

inputs2 = {
    'definition_id2_name' : "card_txn_monthly_sigs",
    'datalayer_name' : "signal_output_layer",
    'search_text' : "season",
    'signal_name' : "cnt_fs_online_trips_season_1"
    }

inputs3 = {
    'search_text' : "txn",
    'definition_id2_name' : "staging.txn_fact.txn_coll",
    'definition_id3_name' : "pos_txn_mstr_raw"
    }

inputs5 = {
    "explorer" : "USE CASE EXPLORER",
    "datalayer_name" : "List Pull - Promo Targeting",
    "search" : "promo",
    "name_value2" : "promo_targeting",
    "fqn_value" : "listpull.promo_targeting.promo_targeting",
    "fqn_value1" : "listpull.common.pop_segment.low_e_pop",
    "fqn_value2" : "listpull.common.sku_selection.ad_version_segment_sku_sigs",
    "fqn_value3" : "listpull.welcome.base_pop_QC",
    "fqn_value4" : "listpull.common.pop_segment.recent_pop",
    "fqn_value5" : "listpull.ob_dynamic.low_e_pop",
    "fqn_value6" : "listpull.listpull_reports.basket_builder",
    "signal_name1" : "Front store total sales amount in past 12 months",
    "signal_name2" : "Segment number of the customer"
}

inputs7 = {
    'datalayer_name' : "signal_output_layer",
    'datalayer_name_2' : "use_case_layer",
    'search_text_1' : "segment",
    'search_text_2' : "group",
    'signal_name' : "sigout.cust_prod_txn_sigs.brief.hh_prod_txn_monthly_sigs",
    'signal_name_1' : "segment_dsc_short",
    'signal_name_2' : "segment_nbr",
    'signal_name_3' : "prod_group_signal_name",
    'fqn' : "sigout.hh_sigs.hh_sigs",
    'fqn_1' : "listpull.listpull_reports.aisle_cross",
    'fqn_2' : "listpull.aisle_cross.cross_sell_cats",
    'fqn_3' : "listpull.aisle_cross.hh_seed_and_rec_top3",
    'fqn_4' : "listpull.loyalist_letter_dm.filter_population",
    'fqn_5' : "listpull.listpull_reports.loyalist_letter_dm",
    'fqn_6' : "sigout.model_score.need_state_model.mst_profiling",
    'fqn_7' : "listpull.loyalist_letter_dm.persona_primary_card",
    'fqn_8' : "sigout.model_score.need_state_model.segment_assertion",
    'fqn_9' : "sigout.read.hh_prod_txn_monthly_brief_sigs",
    'fqn_10' : "sigout.model_input.dm_new_model.dm_hh_sigs",
    'fqn_11' : "sigout.hh_prod_sigs.hh_prod_group_txn_brief_signals",
    'fqn_12' : "sigout.hh_prod_sigs.hh_prod_sigs",
    'fqn_13' : "sigout.hh_sigs.hh_sigs_1",
    'signal_set_name' : "hh_prod_txn_monthly_sigs",
    'relationship_name' : "indicator",
    'subject_name' : "household_product_group",
    'reportName' : "report-1502968160548"
    }

inputs8 = {
    "search1" : "segment",
    "search2" : "group",
    "datalayer_name" : "signal_output_layer",
    "signal_name1" : "sigout.model_score.need_state_model.need_states_profiling",
    "signal_name2" : "sigout.model_score.need_state_sub_seg_scoring.sub_seg_score",
    "signal_name3" : "sigout.cust_prod_txn_sigs.brief.hh_prod_txn_monthly_sigs",
    "signal_name4" : "sigout.cust_prod_txn_sigs.detailed.hh_prod_txn_monthly_sigs",
    "signal_name5" : "dim.customer.customer_segment_dim.customer_segment_dim_coll",
    "description_name" : "Code representing the customer segment",
    "displayName1" : "indicator",
    "displayName2" : "Household * Product Group",
    "displayName3" : "Use Case Layer",
    "displayName4" : "February",
    "fqn_value1" : "sigout.model_score.need_state_model.need_states_profiling.sigout.model_score.need_state_model.need_states_profiling.segment_nbr",
    "fqn_value2" : "sigout.model_score.need_state_sub_seg_scoring.sub_seg_score.sigout.model_score.need_state_sub_seg_scoring.sub_seg_score.segment_nbr",
    "fqn_value3" : "sigout.cust_prod_txn_sigs.brief.hh_prod_txn_monthly_sigs.computeSignals.prod_group_signal_name",
    "fqn_value4" : "sigout.cust_prod_txn_sigs.detailed.hh_prod_txn_monthly_sigs.computeSignals.prod_group_signal_name",
    "id1_name" : "listpull.listpull_reports.aisle_cross",
    "id2_name" : "listpull.aisle_cross.cross_sell_cats",
    "id3_name" : "sigout.hh_sigs.hh_sigs_1",
    "id4_name" : "listpull.aisle_cross.hh_seed_and_rec_top3",
    "id5_name" : "sigout.hh_sigs.hh_sigs",
    "id6_name" : "listpull.loyalist_letter_dm.filter_population",
    "id7_name" : "listpull.listpull_reports.loyalist_letter_dm",
    "id8_name" : "sigout.model_score.need_state_model.mst_profiling",
    "id9_name" : "listpull.loyalist_letter_dm.persona_primary_card",
    "id10_name" : "sigout.model_score.need_state_model.segment_assertion",
    "id11_name" : "listpull.common.pop_segment.low_e_pop",
    "id12_name" : "listpull.welcome.base_pop_QC",
    "id13_name" : "listpull.common.pop_segment.recent_pop",
    "id14_name" : "listpull.ob_dynamic.low_e_pop",
    "id15_name" : "listpull.listpull_reports.basket_builder",
    "id16_name" : "sigout.read.hh_prod_txn_monthly_brief_sigs",
    "id17_name" : "sigout.model_input.dm_new_model.dm_hh_sigs",
    "id18_name" : "sigout.hh_prod_sigs.hh_prod_group_txn_brief_signals",
    "id19_name" : "sigout.hh_prod_sigs.hh_prod_sigs",
    "id21_name" : "sigout.hh_prod_sigs.hh_prod_group_txn_detailed_signals",
    "id23_name" : "sigout.read.hh_prod_txn_monthly_detailed_sigs",
    "reportName" : "report-1502968160548",
    "data" : {
        "clusterData": "true",
    	"s_name": "CVSKCPERFQA",
    	"reportName": "report-1502968160548",
    	"id19_name": "sigout.hh_prod_sigs.hh_prod_sigs",
    	"columns": ["hh_key", "prod_group_key", "prod_group_signal_name", "cnt_fs_trips_mth_2"]
    }
}

inputs9 = {
    "search1" : "segment",
    "search2" : "group",
    "datalayer_name" : "signal_output_layer",
    "description_name" : "Code representing the customer segment",
    "fqn_value1" : "sigout.model_score.need_state_model.need_states_profiling.sigout.model_score.need_state_model.need_states_profiling.segment_nbr",
    "fqn_value2" : "sigout.model_score.need_state_sub_seg_scoring.sub_seg_score.sigout.model_score.need_state_sub_seg_scoring.sub_seg_score.segment_nbr",
    "displayName1" : "indicator",
    "displayName2" : "Channel",
    "signal_name1" : "sigout.cust_prod_txn_sigs.card_prod_txn_trip_sigs.computeSignals.prod_group_signal_name",
    "signal_name2" : "sigout.cust_prod_txn_sigs.card_prod_txn_trip_sigs.computeSignals.prod_grouping_name",
    "signal_name3" : "sigout.model_score.need_state_model.need_states_profiling",
    "signal_name4" : "sigout.model_score.need_state_sub_seg_scoring.sub_seg_score",
    "signal_name5" : "dim.customer.customer_segment_dim.customer_segment_dim_coll",
    "id1_name" : "listpull.listpull_reports.aisle_cross",
    "id2_name" : "listpull.aisle_cross.cross_sell_cats",
    "id3_name" : "sigout.hh_sigs.hh_sigs_1",
    "id4_name" : "listpull.aisle_cross.hh_seed_and_rec_top3",
    "id5_name" : "sigout.hh_sigs.hh_sigs",
    "id6_name" : "listpull.loyalist_letter_dm.filter_population",
    "id7_name" : "listpull.listpull_reports.loyalist_letter_dm",
    "id8_name" : "sigout.model_score.need_state_model.mst_profiling",
    "id9_name" : "listpull.loyalist_letter_dm.persona_primary_card",
    "id10_name" : "sigout.model_score.need_state_model.segment_assertion",
    "id11_name" : "listpull.common.pop_segment.low_e_pop",
    "id12_name" : "listpull.welcome.base_pop_QC",
    "id13_name" : "listpull.common.pop_segment.recent_pop",
    "id14_name" : "listpull.ob_dynamic.low_e_pop",
    "id15_name" : "listpull.listpull_reports.basket_builder",
    "id16_name" : "sigout.cust_prod_txn_sigs.card_prod_txn_trip_sigs.computeSignals.prod_group_signal_name",
    "data" : {
    	"clusterData": "true",
    	"s_name": "CVSQA2",
    	"reportName": "report-1503047695253",
    	"view": "sigout.cust_prod_txn_sigs.card_prod_txn_trip_sigs",
    	"columns": ["xtra_card_nbr", "prod_group_key", "store_nbr", "txn_nbr", "txn_datetime_key", "reg_nbr", "prod_group_signal_name", "prod_grouping_name"]
    }
}

inputs11 = {
    'search_text' : "email",
    'subject_1' : "consumer",
    'subject_2' : "household",
    'signal_name' : "cnt_click_cmpgn_em_p12m",
    'definition_id2_name' : "hh_cpn_monthly_sigs"
    }
