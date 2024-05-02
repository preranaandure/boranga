import ExternalConservationStatusDash from '../conservation_status/dashboard.vue'
import ConservationStatusProposal from '../conservation_status/conservation_status_proposal.vue'
import ConservationStatusProposalSubmit from '../conservation_status/conservation_status_proposal_submit.vue'
import ExternalOccurrenceReportDash from '../occurrence/dashboard.vue'
import OccurrenceReportProposal from '../occurrence/occurrence_report_proposal.vue'
import OCRProposalSubmit from '../occurrence/ocr_proposal_submit.vue'

export default
    {
        path: '/external',
        component:
        {
            render(c) {
                return c('router-view')
            }
        },
        children: [
            {
                path: 'conservation-status',
                component: ExternalConservationStatusDash,
                name: "external-conservation_status-dash"
            },
            {
                path: 'occurrence-report',
                component: ExternalOccurrenceReportDash,
                name: "external-occurrence_report-dash"
            },
            {
                path: 'occurrence-report/:occurrence_report_id',
                component: OccurrenceReportProposal,
                name: "draft_ocr_proposal"
            },
            {
                path: 'occurrence-report/submit',
                component: OCRProposalSubmit,
                name: "submit_ocr_proposal"
            },
            {
                path: 'conservation_status',
                component: {
                    render(c) {
                        return c('router-view')
                    },
                },
                children: [
                    {
                        path: ':conservation_status_id',
                        component: ConservationStatusProposal,
                        name: "draft_cs_proposal"
                    },
                    {
                        path: 'submit',
                        component: ConservationStatusProposalSubmit,
                        name: "submit_cs_proposal"
                    },
                ]
            },
        ]
    }
