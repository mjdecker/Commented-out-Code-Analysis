    int x, y;   
                               m14));
                      encoding_prefix(tok->enc),
                      encoding_prefix(tok->enc),
                      quote_char(tok->c));
                      quote_cstring(tok->sval));
                      ty2s(node->ty), node2s(node));
                    break;
                    break;
                    buf_printf(b, ",");
                    emit("mov %d(#rbp), #al", arg++ * 8);
                    emit("mov %d(#rbp), #rax", arg++ * 8);
                    emit("movzb #%s, #%s", SREGS[ireg], MREGS[ireg]);
                    emit("movzb #al, #eax");
                    vec_append(r, arg);
                    vec_pop(r);
                    vec_push(r, vec_get(arg, i));
                   node->declvar->varname);
                   node->kind == AST_FUNCALL ? node->fname : node2s(node));
                   node2s(node->cond),
                   node2s(node->cond),
                   node2s(node->els));
                   node2s(node->operand));
                   node2s(node->then));
                   node2s(node->then),
                   ty2s(node->declvar->ty),
                   ty2s(node->operand->ty),
                   ty2s(node->ty),
                  2 +) 10);
                 float v06, float v07, float v08, float v09, float v10,
                 float v11, float v12, float v13, float v14, float v15,
                 float v16, float v17) {
                *p = ' ';
                17.0);
                9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0,
                align = val;
                arg->ty;
                base = base->operand;
                break;
                break;
                break;
                break;
                buf_printf(b, " (%s)", do_ty2s(dict, fieldtype));
                buf_printf(b, "%s", do_ty2s(dict, t));
                buf_printf(b, ",");
                buf_printf(b, ",");
                char *key = vec_get(keys, i);
                char *s = vec_get(keys, i++);
                col += TAB - 1;
                continue;
                continue;
                continue;
                continue;
                continue;
                data |= ((((long)1 << totype->bitsize) - 1) & eval_intexpr(v, NULL)) << totype->bitoff;
                else
                emit(".quad %u", v);
                emit("mov %d(#rbp), #rax", arg++ * 8);
                error("flexible member may only appear as the last member: %s %s", ty2s(ty), name);
                error("flexible member with no other fields: %s %s", ty2s(ty), name);
                error("global variable expected, but got %s", node2s(base));
                error("pointer type expected, but got %s %s",
                errort(tok, ", expected, but got %s", tok2s(tok));
                errort(tok, "array designator exceeds array bounds: %d", idx);
                errort(tok, "at least one parameter is required before \"...\"");
                errort(tok, "default expression specified twice");
                errort(tok, "field does not exist: %s", tok2s(tok));
                errort(tok, "function expected, but got %s", node2s(node));
                errort(tok, "malformed desginated initializer: %s", tok2s(tok));
                errort(tok, "negative alignment: %d", val);
                expect(';');
                fieldtype->bitoff = 0;
                fieldtype->bitoff = bitoff;
                fieldtype->offset = off;
                fieldtype->offset = off;
                finish_bitfield(&off, &bitoff);
                for (int i = 1; i < vec_len(arg); i++)
                glue_push(r, vec_head(arg));
                goto errcheck;
                i++;
                if (i > 0)
                if (node->totype->bitsize <= 0) {
                if (strcmp(fieldname, s) == 0)
                if (usertype) goto err;
                if (v->ty->kind == KIND_BOOL)
                if (v->ty->kind == KIND_BOOL) {
                if (vec_len(arg) > 0)
                is_inttype(arg->ty) ? type_int :
                m->nused++;
                node = vec_get(inits, i);
                off += compute_padding(off, fieldtype->align);
                push("rax");
                push("rax");
                push(REGS[ireg++]);
                push_xmm(xreg++);
                return c;
                return false;
                subst = copy_token(subst);
                subst->space = tok->space;
                totype = node->totype;
                Type *fieldtype = dict_get(ty->fields, key);
                Type *t = vec_get(ty->params, i);
                unget_token(tok);
                unget_token(tok);
                usertype = def;
                v = node->initval;
                vec_append(r, arg);
                vec_push(block, ast_decl(var, NULL));
                vec_push(block, ast_decl(var, read_decl_init(ty)));
                vec_push(r, subst);
                warnt(peek(), "missing ';' at the end of field list");
                }
                }
                } else {
             float:F, double:D, ldouble:LD)
            "One of -a, -c, -E or -S must be specified.\n\n");
            "Usage: 8cc [ -E ][ -a ] [ -h ] <file>\n\n"
            *addr = conv(node);
            *align = MAX(*align, fieldtype->align);
            *defaultexpr = read_assignment_expr();
            *ellipsis = true;
            *end = true;
            *q++ = *p++;
            *q++ = *p++;
            a2s_declinit(b, node->declinit);
            a2s_declinit(b, node->lvarinit);
            arg += size / 8;
            arg = ast_conv(paramtype, arg);
            assert(node->totype->bitoff == 0);
            assert(param->kind == AST_LVAR);
            assert(ty->ptr);
            assign_string(inits, ty, tok->sval, off);
            assign_string(inits, ty, tok->sval, off);
            ast_typedef(ty, name);
            bitoff += fieldtype->bitsize;
            bitoff = 0;
            buf[i++] = '%';
            buf[i++] = '%';
            buf[i++] = *p;
            buf_printf(b, " %s", node2s(node->els));
            buf_printf(b, " -> ");
            buf_printf(b, "%d", node->ival);
            buf_printf(b, "%f", node->fval);
            buf_printf(b, "%ldL", node->ival);
            buf_printf(b, "%lldL", node->ival);
            buf_printf(b, "%s %s", ty2s(param->ty), node2s(param));
            buf_printf(b, "%s", node2s(vec_get(node->args, i)));
            buf_printf(b, "(");
            buf_printf(b, "(%c ", node->kind);
            buf_printf(b, "(%s", kind);
            buf_printf(b, "(== ");
            buf_printf(b, ")");
            buf_printf(b, ")");
            buf_printf(b, ";");
            buf_printf(b, "\"%s\"", quote_cstring(node->sval));
            buf_printf(cppdefs, "#define %s\n", optarg);
            buf_printf(cppdefs, "#undef %s\n", optarg);
            buf_write(b, ' ');
            Buffer *b = make_buffer();
            char *name = NULL;
            char *p = strchr(optarg, '=');
            close_file(vec_pop(files));
            designated = true;
            designated = true;
            dict_put(r, name, fieldtype);
            dict_put(r, name, fieldtype);
            do_emit_data(v->lvarinit, v->ty->size, 0, depth);
            do_node2s(b, vec_get(node->stmts, i));
            else buf_printf(b, "'%c'", node->ival);
            else goto err;
            else if (node->ival == '\0') buf_printf(b, "'\\0'");
            else if (node->ival == '\\') buf_printf(b, "'\\\\'");
            else if (size == klong) size = kllong;
            emit(".long %d", *(uint32_t *)&fval);
            emit(".quad %lu", *(uint64_t *)&node->fval);
            emit(".quad %s", val->glabel);
            emit(".quad %s", val->newlabel);
            emit(".quad %s+%u", base->glabel, v * ty->ptr->size);
            emit(".string \"%s\"", quote_cstring_len(node->sval, node->ty->size - 1));
            emit("lea %d(#rbp), #rax", arg * 8);
            emit("lea %s(#rip), #rax", label);
            emit("lea %s+%d(#rip), #rax", label, off);
            emit("mov #edx, #eax");
            emit("ucomisd #xmm0, #xmm1");
            emit("ucomiss #xmm0, #xmm1");
            emit_addr(v);
            emit_data_addr(v->operand, depth);
            emit_data_charptr(val->operand->sval, depth);
            emit_data_primtype(totype, &(Node){ AST_LITERAL, totype, .ival = data }, depth);
            emit_expr(node->initval);
            emit_expr(v);
            emit_expr(v);
            emit_label(node->flabel);
            emit_label(node->flabel);
            emit_label(node->newlabel);
            emit_label(node->slabel);
            emit_lsave(node->totype, node->initoff + off);
            emit_noindent(".data");
            emit_noindent(".text");
            emit_noindent(".text");
            emit_noindent(".text");
            emit_save_literal(node->initval, node->totype, node->initoff + off);
            emit_toplevel(v);
            emit_zero_filler(lastend + off, node->initoff + off);
            enc = enc2;
            ensure_lvalue(node);
            ensure_lvalue(node);
            ensure_not_void(fieldtype);
            ensure_not_void(ty);
            ensure_not_void(ty);
            error("as failed");
            error("declarations of %s does not match", tag);
            error("duplicate case value: %d", x->beg);
            error("internal error");
            error("invalid pointer arith");
            error("invalid UTF-8 continuation byte");
            error("premature end of input");
            error("premature end of input");
            error("premature end of input");
            error("stray %s: %s", src->kind == AST_GOTO ? "goto" : "unary &&", label);
            errort(hash, "premature end of header name");
            errort(ident, "unterminated macro argument list");
            errort(name, "missing ')' in macro parameter list");
            errort(peek(), "';' or ',' are expected, but got %s", tok2s(peek()));
            errort(peek(), "K&R-style declarator expected, but got %s", tok2s(peek()));
            errort(tok, "case region is not in correct order: %d ... %d", beg, end);
            f->p++;
            fieldname = tok->sval;
            fieldname = vec_get(keys, i++);
            fieldtype = copy_type(fieldtype);
            fieldtype = dict_get(ty->fields, fieldname);
            fieldtype = dict_get(ty->fields, fieldname);
            fieldtype->bitoff = 0;
            fieldtype->bitsize = next_token(':') ? read_bitsize(name, fieldtype) : -1;
            fieldtype->offset = off;
            finish_bitfield(&off, &bitoff);
            finish_bitfield(&off, &bitoff);
            finish_bitfield(&off, &bitoff);
            float fval = node->fval;
            for (i++ ; i < vec_len(inits); i++) {
            for (int i = 0; i < vec_len(keys); i++) {
            for (int i = 0; i < vec_len(ty->params); i++) {
            for (q--; q[-1] != '/'; q--);
            functype->hasva = false;
            get();
            glue_push(r, t1);
            hideset = t1->hideset;
            hideset = t1->hideset;
            i = 0;
            i = idx;