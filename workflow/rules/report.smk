"""A small, reproducible starter rule. Replace it with the first real stage."""


rule render_report:
    input:
        config["example_input"],
    output:
        config["report"],
    log:
        "logs/render_report.log",
    conda:
        "../envs/base.yaml"
    params:
        project_name=config["project_name"],
    shell:
        "(printf 'Project: %s\\n\\nInput:\\n' {params.project_name:q}; cat {input:q})"
        " > {output:q} 2> {log:q}"
